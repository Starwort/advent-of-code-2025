from collections import Counter, defaultdict, deque
from math import prod

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

raw = aoc_helper.fetch(8, 2025)


def parse_raw(raw: str):
    return extract_ints(raw).chunked(3)


data = parse_raw(raw)

Loc = tuple[int, int, int]


def sqr_dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data, count: int = 1000):
    circuits: dict[Loc, set[Loc]] = (
        data.mapped(lambda loc: (loc, {loc})).iter().collect(dict)
    )
    j = 0
    for a, b in data.combinations(2).sorted(lambda locs: sqr_dist(*locs)):
        j += 1
        if j > count:
            break
        for i in circuits[a] | circuits[b]:
            circuits[i] |= circuits[a] | circuits[b]
    largest = []
    for i in sorted(circuits.values(), key=len, reverse=True):
        if i not in largest:
            largest.append(i)
            if len(largest) == 3:
                return prod(len(i) for i in largest)


test1 = part_one(
    parse_raw(
        """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    ),
    count=10,
)
assert test1 == 40, test1
aoc_helper.lazy_test(day=8, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    circuits: dict[Loc, set[Loc]] = (
        data.mapped(lambda loc: (loc, {loc})).iter().collect(dict)
    )
    for a, b in data.combinations(2).sorted(lambda locs: sqr_dist(*locs)):
        if a in circuits[b]:
            continue
        for i in circuits[a] | circuits[b]:
            circuits[i] |= circuits[a] | circuits[b]
        if len(circuits[a]) == len(data):
            return a[0] * b[0]


aoc_helper.lazy_test(day=8, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=8, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=8, year=2025, solution=part_two, data=data)
