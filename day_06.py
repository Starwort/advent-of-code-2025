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
    numbers = list(numbers).mapped(extract_ints).transposition()
    ops = list(re.findall(r"\+|\*", ops))
    return numbers, ops


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    numbers, ops = data
    return (
        numbers.zipped(ops)
        .mapped(
            lambda nums_op: nums_op[0].sum() if nums_op[1] == "+" else nums_op[0].prod()
        )
        .sum()
    )


aoc_helper.lazy_test(day=6, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    numbers, ops = data
    lines = list(raw.splitlines()[:-1])
    start = 0
    result = 0
    for op, nums in zip(ops, numbers):
        width = nums.mapped(str).mapped(len).max()
        each_num = (
            lines.mapped(lambda line: list(line[start : start + width]))
            .transposition()
            .mapped("".join)
            .mapped(int)
        )
        start += width + 1
        if op == "+":
            result += each_num.sum()
        else:
            result += each_num.prod()
    return result


# aoc_helper.lazy_test(day=6, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=6, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=6, year=2025, solution=part_two, data=data)
