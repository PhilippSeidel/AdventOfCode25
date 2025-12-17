import numpy as np

def is_invalid(id):
    id = [int(d) for d in str(id)]
    for l in range(int(len(id)/2)):
        mask_length = int(len(id)/2) - l
        residue_length = len(id) - mask_length
        if residue_length % mask_length == 0:
            mask = np.array(id[:mask_length] * int(residue_length/mask_length))
            residue_id = np.array(id[mask_length:])
            if not np.any(residue_id - mask):
                return True
    return False

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
        print(f'current count: {len(invalid_ids)}')
    print(invalid_ids)
    print(sum(invalid_ids))