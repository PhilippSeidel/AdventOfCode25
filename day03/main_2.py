import numpy as np

def highest_num(bank):
    num = 0
    left_idx = -1
    bank += [0]
    for bats_left in range(12, 0, -1):
        available_bats = bank[(left_idx + 1):-bats_left]
        bat_idx = np.argmax(available_bats)
        left_idx += bat_idx + 1
        num += available_bats[bat_idx] * (10**(bats_left - 1))
    return num


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