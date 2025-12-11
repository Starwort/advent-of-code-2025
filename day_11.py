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

raw = aoc_helper.fetch(11, 2025)


def parse_raw(raw: str):
    return dict(
        list(raw.splitlines())
        .mapped(lambda i: i.split(": "))
        .mapped(lambda pair: (pair[0], list(pair[1].split())))
    )


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data: dict[str, list[str]] = data):
    paths = defaultdict(int)
    paths["you"] = 1
    now = {"you"}
    while now and now != {"out"}:
        next_now = set()
        for server in now:
            if server == "out":
                continue
            count = paths.pop(server)
            for next in data[server]:
                paths[next] += count
                next_now.add(next)
        now = next_now
    return paths["out"]


aoc_helper.lazy_test(day=11, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data: dict[str, list[str]] = data):
    paths = defaultdict(int)
    paths["svr", False, False] = 1
    now = {("svr", False, False)}
    while now:
        next_now = set()
        for server, fft, dac in now:
            if server == "out":
                continue
            count = paths.pop((server, fft, dac))
            if server == "fft":
                fft = True
            if server == "dac":
                dac = True
            for next in data[server]:
                paths[next, fft, dac] += count
                next_now.add((next, fft, dac))
        now = next_now
    return paths["out", True, True]


aoc_helper.lazy_test(day=11, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=11, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=11, year=2025, solution=part_two, data=data)
