import copy


def parse_input(input_file: str) -> list[str]:
    with open(input_file) as input:
        input = input.readlines()
    all_lines = []
    for line in input:
        all_lines.append(repr(line))
    return all_lines


spooky_map = {
    "eerie": "0",
    "witch": "1",
    "ghoul": "2",
    "goblin": "3",
    "howl": "4",
    "lurking": "5",
    "cackle": "6",
    "vile": "7",
    "vampire": "8",
    "petrify": "9",
}


def find_digit(word_or_digit: str) -> str:
    if word_or_digit.isdigit():
        return word_or_digit
    return spooky_map[word_or_digit]


def decode_single_coord(line: str) -> int:
    last_digit_index = 100
    first_digit_index = 100

    for word_or_digit in list(spooky_map.keys()) + list(spooky_map.values()):
        word_distance_from_start = line.find(word_or_digit)
        word_distance_from_end = line[::-1].find(word_or_digit[::-1])

        if (
            word_distance_from_start > -1
            and word_distance_from_start < first_digit_index
        ):
            first_digit_index = word_distance_from_start
            first_word_or_digit = word_or_digit

        if word_distance_from_end > -1 and word_distance_from_end < last_digit_index:
            last_digit_index = word_distance_from_end
            last_word_or_digit = word_or_digit

    full_number = find_digit(first_word_or_digit) + find_digit(last_word_or_digit)

    return int(full_number)


def decode_all_coords(all_lines: list[str]) -> list[tuple[int]]:
    encoded_coords = [
        (all_lines[i], all_lines[i + 1]) for i in range(0, len(all_lines), 2)
    ]
    decoded_coords = []
    for encoded_row, encoded_column in encoded_coords:
        decoded_coords.append(
            (decode_single_coord(encoded_row), decode_single_coord(encoded_column))
        )
    return decoded_coords


def find_grid_size(decoded_coords: list[tuple[int]]) -> tuple[int]:
    row_indices = [x for (x, _) in decoded_coords]
    column_indices = [y for (_, y) in decoded_coords]
    return max(row_indices) + 1, max(column_indices) + 1


def create_grid(max_indices: tuple[int]) -> list[str]:
    max_row, max_column = max_indices
    row = " " * max_column
    return [row] * max_row


def plot_points(max_indices: tuple[int], decoded_coords: list[tuple[int]]) -> list[str]:
    grid = create_grid(max_indices)
    for row, column in decoded_coords:
        grid[row] = grid[row][:column] + "x" + grid[row][column + 1 :]
    return grid


def find_solution(input_file: str) -> list[str]:
    all_lines = parse_input(input_file)
    decoded_coords = decode_all_coords(all_lines)
    max_indices = find_grid_size(decoded_coords)
    for line in plot_points(max_indices, decoded_coords):
        print(line)


if __name__ == "__main__":
    print("example 1")
    find_solution("example_1_input.txt")
    print("example 2")
    find_solution("example_2_input.txt")
    print("example 3")
    find_solution("example_3_input.txt")
    find_solution("aled_input.txt")
