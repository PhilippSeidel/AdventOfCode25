def count_neighbours(rolls, num_cols, num_rows, idx):
    roll_count = 0
    (x, y) = idx
    up_left = [max(0, x - 1), max(0, y - 1)]
    low_right = [min(num_cols - 1, x + 1), min(num_rows - 1, y + 1)]
    for x_n in range(up_left[0], low_right[0] + 1):
        for y_n in range(up_left[1], low_right[1] + 1):
            if (not ( x_n == x and y_n == y)) and rolls[y_n][x_n] == '@':
                roll_count += 1
    return roll_count


def remove_accessible_rolls(rolls, num_cols, num_rows):
    removal_count = 0
    for x in range(num_cols):
        for y in range(num_rows):
            if rolls[y][x] != '@':
                continue
            neighbour_count = count_neighbours(rolls, num_cols, num_rows, (x, y))
            if neighbour_count < 4:
                removal_count += 1
                rolls[y][x] = 'X'
    print(f'removed {removal_count} rolls')
    return removal_count


with open('input/input') as input:
    rolls = [list(row) for row in input.read().split("\n")]
    num_cols = len(rolls[0])
    num_rows = len(rolls)
    removal_count = 0
    while True:
        current_removal_count = remove_accessible_rolls(rolls, num_cols, num_rows)
        if current_removal_count == 0:
            break
        removal_count += current_removal_count
    print(removal_count)