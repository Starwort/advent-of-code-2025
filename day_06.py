import re
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

raw = aoc_helper.fetch(6, 2025)


def parse_raw(raw: str):
    *numbers, ops = raw.splitlines()
    numbers2 = list(
        re.split(
            r"\n\s*\n",
            "\n".join(list(numbers).mapped(list).transposition().mapped("".join)),
        )
    ).mapped(extract_ints)
    numbers = list(numbers).mapped(extract_ints).transposition()
    ops = list(re.findall(r"\+|\*", ops))
    return numbers, ops, numbers2


data = parse_raw(raw)


def calculate(nums: list[list[int]], ops: list[str]) -> int:
    return (
        iter(zip(nums, ops))
        .map(
            lambda nums_op: nums_op[0].sum() if nums_op[1] == "+" else nums_op[0].prod()
        )
        .sum()
    )


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    numbers, ops, _ = data
    return calculate(numbers, ops)


aoc_helper.lazy_test(day=6, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    _, ops, numbers = data
    return calculate(numbers, ops)


# aoc_helper.lazy_test(day=6, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2025, solution=part_two, data=data)
