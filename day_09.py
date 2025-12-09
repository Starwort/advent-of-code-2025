from collections import Counter, defaultdict, deque

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
from shapely import Polygon

raw = aoc_helper.fetch(9, 2025)


def parse_raw(raw: str):
    places = extract_ints(raw).chunked(2)
    grid = SparseGrid(bool)
    for x, y in places:
        grid[x, y] = True
    return grid, places


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    grid, _ = data
    best = 0
    for (pos, a), (pos2, b) in grid.items().combinations(2):
        if not a or not b:
            continue
        area = (abs(pos[0] - pos2[0]) + 1) * (abs(pos[1] - pos2[1]) + 1)
        if area > best:
            best = area
    return best


aoc_helper.lazy_test(day=9, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data: tuple[SparseGrid[bool], list[tuple[int, int]]] = data):
    _, places = data
    polygon = Polygon(places)
    rect = lambda a, b: Polygon([a, (a[0], b[1]), b, (b[0], a[1])])
    best = 0
    for a, b in places.combinations(2).filtered(lambda ab: polygon.covers(rect(*ab))):
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if area > best:
            best = area
    return best


aoc_helper.lazy_test(day=9, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=9, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=9, year=2025, solution=part_two, data=data)
