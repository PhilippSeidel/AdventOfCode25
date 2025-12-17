import math

def is_invalid(id):
    id = [int(d) for d in str(id)]
    return id[:int(len(id)/2)] == id[int(len(id)/2):]


def invalid_ids_in_ranges(lower_bound, upper_bound):
    invalid_ids = []
    for id in range(lower_bound, upper_bound + 1):
        if is_invalid(id):
            invalid_ids.append(id)
    return invalid_ids

with open('input/input') as input:
    ranges = []
    invalid_ids = []
    for range_str in input.read().split(","):
        ranges.append([int(range_str.split("-")[0]), int(range_str.split("-")[1])])
    for r in ranges:
        invalid_ids += invalid_ids_in_ranges(r[0], r[1])
    print(invalid_ids)
    print(sum(invalid_ids))