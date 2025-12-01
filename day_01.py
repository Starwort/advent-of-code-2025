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

raw = aoc_helper.fetch(1, 2025)


def parse_raw(raw: str):
    return list(raw.splitlines()).mapped(
        lambda line: (line[0] == "R", extract_ints(line)[0])
    )


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    pos = 50
    password = 0
    for right, steps in data:
        if right:
            pos += steps
        else:
            pos -= steps
        pos %= 100
        if pos == 0:
            password += 1
    return password


aoc_helper.lazy_test(day=1, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    pos = 50
    password = 0
    for right, steps in data:
        loops, steps = divmod(steps, 100)
        password += loops
        if right:
            if pos >= 100 - steps:
                password += 1
            pos += steps
        else:
            if pos <= steps and pos != 0:
                password += 1
            pos -= steps
        pos %= 100
    return password


aoc_helper.lazy_test(
    day=1,
    year=2025,
    parse=parse_raw,
    solution=part_two,
    test_data=(
        """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""",
        6,
    ),
)

aoc_helper.lazy_submit(day=1, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2025, solution=part_two, data=data)
