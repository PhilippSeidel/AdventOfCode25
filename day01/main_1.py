position = 50
zero_counter = 0
with open('input/input') as input:
    instructions = input.read().split('\n')
    for instruction in instructions:
        old_pos = position
        if instruction[0] == 'L':
            position = (position - int(instruction[1:])) % 100
        else:
            position = (position + int(instruction[1:])) % 100
        if position == 0:
            zero_counter += 1

        print(f'instruction: {instruction}: {old_pos} --> {position}, zeros: {zero_counter}')
