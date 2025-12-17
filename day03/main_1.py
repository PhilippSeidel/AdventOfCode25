import numpy as np

def highest_num(bank):
    left_idx = np.argmax(bank[:-1])
    right = np.max(bank[(left_idx + 1):])
    return bank[left_idx] * 10 + right


with open('input/input') as input:
    banks = []
    highest_num_sum = 0
    for bank_str in input.read().split("\n"):
        banks.append([int(d) for d in str(bank_str)])
    for bank in banks:
        highest = highest_num(bank)
        print(f'bank {bank} --> highest: {highest}')
        highest_num_sum += highest
    print(f'sum: {highest_num_sum}')