from collections import Counter, defaultdict, deque
from itertools import count

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
import z3

raw = aoc_helper.fetch(10, 2025)


def parse_raw(raw: str):
    lines = raw.splitlines()
    out = list[tuple[list[bool], list[list[int]], list[int]]]()
    for line in lines:
        lights, *buttons, joltages = line.split()
        lights = list(lights[1:-1]).mapped(lambda c: c == "#")
        buttons = list(buttons).mapped(lambda b: extract_ints(b))
        joltages = extract_ints(joltages)
        out.append((lights, buttons, joltages))
    return out


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    total = 0
    for lights, buttons, _ in data:
        if lights.none():
            continue
        for i in count(1):
            for my_buttons in buttons.combinations(i):
                test = list(False for _ in lights)
                for button in my_buttons:
                    for pos in button:
                        test[pos] = not test[pos]
                if test == lights:
                    total += i
                    break
            else:
                continue
            break
    return total


aoc_helper.lazy_test(day=10, year=2025, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    total = 0
    for _, buttons, joltages in data:
        solver = z3.Optimize()
        variables = [z3.Int(f"x{i}") for i in range(len(buttons))]
        used = defaultdict(int)
        for var, button in zip(variables, buttons):
            solver.add(var >= 0)
            for pos in button:
                used[pos] = used[pos] + var
        for pos, count in enumerate(joltages):
            solver.add(used[pos] == count)
        solver.minimize(sum(variables))
        if solver.check() == z3.sat:
            model = solver.model()
            total += sum(model[var].as_long() for var in variables)
    return total


aoc_helper.lazy_test(day=10, year=2025, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2025, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2025, solution=part_two, data=data)
