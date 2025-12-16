import math

position = 50
zero_counter = 0
with open('input/input') as input:
    instructions = input.read().split('\n')
    for instruction in instructions:
        old_pos = position
        distance = int(instruction[1:])
        if instruction[0] == 'L':
            position -= distance
            old_pos = 100 - old_pos
        else:
            position += distance

        zero_passes = math.floor((position + old_pos) / 100)

        position %= 100
        zero_counter += zero_passes

        print(f'instruction: {instruction}: {old_pos} --> {position}, zero_passes: {zero_passes}, zeros: {zero_counter}')
