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

raw = aoc_helper.fetch(4, 2025)


def parse_raw(raw: str):
    return Grid.from_string(raw, lambda i: i == "@")


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    total = 0
    for y, row in data.data.enumerated():
        for x, cell in row.enumerated():
            if cell and data.neighbours(x, y).mapped(lambda i: i[1]).sum() < 4:
                total += 1
    return total


aoc_helper.lazy_test(day=4, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    did_change = True
    total = 0
    while did_change:
        did_change = False
        for y, row in data.data.enumerated():
            for x, cell in row.enumerated():
                if cell and data.neighbours(x, y).mapped(lambda i: i[1]).sum() < 4:
                    total += 1
                    data.data[y][x] = False
                    did_change = True
    return total


aoc_helper.lazy_test(day=4, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2025, solution=part_two, data=data)
