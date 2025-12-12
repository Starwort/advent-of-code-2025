from collections import Counter, defaultdict, deque
from functools import cache

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(12, 2025)


def parse_raw(raw: str):
    *shapes, regions = raw.split("\n\n")
    shapes = list(shapes).mapped(
        lambda shape: Grid.from_string(shape.split("\n", 1)[1])
    )
    regions = list(regions.splitlines()).mapped(
        lambda line: list(line.split(":")).mapped(extract_ints)
    )
    return shapes, regions


data = parse_raw(raw)


@cache
def try_solve_region(
    shapes: tuple[Grid[bool]], grid: tuple[tuple[bool, ...]], presents: tuple[int]
) -> bool:
    if not any(presents):
        return True
    max_x = max(len(grid[0]) for grid in shapes)
    max_y = max(len(grid.data) for grid in shapes)
    for i, (shape, times_to_fit) in enumerate(zip(shapes, presents)):
        if times_to_fit:
            for rotation in range(4):
                rotated_shape = shape
                flipped_shape = shape.transpose()
                for _ in range(rotation):
                    rotated_shape = rotated_shape.rotate_clockwise()
                    flipped_shape = flipped_shape.rotate_clockwise()
                for candidate_shape in (rotated_shape, flipped_shape):
                    for y in range(len(grid) - len(candidate_shape.data) + 1):
                        for x in range(len(grid[0]) - len(candidate_shape[0]) + 1):
                            if (
                                x >= max_x
                                and y >= max_y
                                and not any(any(row[:max_x]) for row in grid[:max_y])
                            ):
                                return False
                            if not any(
                                grid[y + dy][x + dx] and candidate_shape.data[dy][dx]
                                for dy in range(len(candidate_shape.data))
                                for dx in range(len(candidate_shape[0]))
                            ):
                                new_grid = tuple(
                                    tuple(
                                        grid[gy][gx]
                                        or (
                                            x <= gx < x + len(candidate_shape[0])
                                            and y <= gy < y + len(candidate_shape.data)
                                            and candidate_shape.data[gy - y][gx - x]
                                        )
                                        for gx in range(len(grid[0]))
                                    )
                                    for gy in range(len(grid))
                                )
                                new_presents = list(presents)
                                new_presents[i] -= 1
                                if try_solve_region(
                                    shapes, new_grid, tuple(new_presents)
                                ):
                                    return True
    return False


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data: tuple[list[Grid[bool]], list[list[list[int]]]] = data):
    shapes, regions = data
    sizes = shapes.mapped(lambda shape: shape.data.mapped(sum).sum())
    shapes = tuple(shapes)
    count = 0
    for dimensions, presents in regions:
        if (
            dimensions.prod()
            < iter(zip(sizes, presents)).map(lambda sp: sp[0] * sp[1]).sum()
        ):
            continue
        # assume that all are solvable for now
        count += 1
        continue
        grid = tuple(
            tuple(False for _ in range(dimensions[0])) for _ in range(dimensions[1])
        )
        if try_solve_region(shapes, grid, tuple(presents)):
            print(
                "Found solution for region with dimensions",
                dimensions,
                "and presents",
                presents,
            )
            count += 1
        else:
            print(
                "No solution for region with dimensions",
                dimensions,
                "and presents",
                presents,
            )
    return count


# aoc_helper.lazy_test(day=12, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    return 0


aoc_helper.lazy_test(day=12, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=12, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=12, year=2025, solution=part_two, data=data)
