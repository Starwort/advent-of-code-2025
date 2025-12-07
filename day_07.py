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

raw = aoc_helper.fetch(7, 2025)


def parse_raw(raw: str):
    return Grid.from_string(raw, str)


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    start = (0, 0)
    for y, row in data.data.enumerated():
        for x, cell in row.enumerated():
            if cell == "S":
                start = (x, y)
                break
    splits = 0
    todo = deque([start])
    visited = set()
    while todo:
        x, y = todo.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if y >= data.data.len() - 1:
            continue
        if data[y + 1][x] == "^":
            splits += 1
            todo.append((x + 1, y + 1))
            todo.append((x - 1, y + 1))
        else:
            todo.append((x, y + 1))
    return splits


aoc_helper.lazy_test(day=7, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    start = (0, 0)
    for y, row in data.data.enumerated():
        for x, cell in row.enumerated():
            if cell == "S":
                start = (x, y)
                break
    splits = 0
    todo = deque([(start, 1)])
    while todo:
        (x, y), count = todo.popleft()
        if y >= data.data.len() - 1:
            splits += count
            continue
        if data[y + 1][x] == "^":
            for i, (pos, other_count) in enumerate(todo):
                if pos == (x + 1, y + 1):
                    todo[i] = (pos, other_count + count)
                    break
            else:
                todo.append(((x + 1, y + 1), count))
            for i, (pos, other_count) in enumerate(todo):
                if pos == (x - 1, y + 1):
                    todo[i] = (pos, other_count + count)
                    break
            else:
                todo.append(((x - 1, y + 1), count))
        else:
            todo.append(((x, y + 1), count))
    return splits


aoc_helper.lazy_test(day=7, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2025, solution=part_two, data=data)
