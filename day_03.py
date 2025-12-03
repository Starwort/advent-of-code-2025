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

raw = aoc_helper.fetch(3, 2025)


def parse_raw(raw: str):
    return list(raw.splitlines()).mapped(list).mapped_each(int)


data = parse_raw(raw)


def optimise_bank(bank, n_left):
    if n_left != 1:
        n_left -= 1
        first = max(bank[:-n_left])
        where = bank.index(first)
        first *= 10**n_left
        return first + optimise_bank(bank[where + 1 :], n_left)
    else:
        return max(bank)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    total = 0
    for bank in data:
        first_digit = max(bank[:-1])
        where = bank.index(first_digit)
        second_digit = max(bank[where + 1 :])
        total += first_digit * 10 + second_digit
    return total


aoc_helper.lazy_test(day=3, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    return data.mapped(lambda bank: optimise_bank(bank, 12)).sum()


aoc_helper.lazy_test(day=3, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2025, solution=part_two, data=data)
