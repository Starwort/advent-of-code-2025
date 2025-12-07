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
    beams = set()
    total = 0
    for row in data.data:
        for x, cell in row.enumerated():
            if cell == "S":
                beams.add(x)
            elif cell == "^":
                if x in beams:
                    beams.remove(x)
                    beams.add(x - 1)
                    beams.add(x + 1)
                    total += 1
    return total


aoc_helper.lazy_test(day=7, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    beams = defaultdict(int)
    for row in data.data:
        for x, cell in row.enumerated():
            if cell == "S":
                beams[x] += 1
            elif cell == "^":
                count = beams.pop(x, 0)
                beams[x - 1] += count
                beams[x + 1] += count
    return sum(beams.values())


aoc_helper.lazy_test(day=7, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2025, solution=part_two, data=data)
