import random
import string
from typing import Callable


def transform_image(text_file: str) -> list[str]:
    with open(text_file) as image:
        all_lines = image.readlines()
        transformed_image = []
    for line in all_lines:
        new_line = ""
        for character in line:
            if character.isspace():
                new_line += " "
            else:
                new_line += "x"
        transformed_image.append(new_line)
    return transformed_image


def get_coords(image: list[str]) -> list[tuple[int]]:
    all_coords = []
    for row_index, line in enumerate(image):
        for column_index, char in enumerate(line):
            if not char.isspace():
                char_coord = (row_index, column_index)
                all_coords.append(char_coord)
    return all_coords


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

spooky_word = {
    "0": "eerie",
    "1": "witch",
    "2": "ghoul",
    "3": "goblin",
    "4": "howl",
    "5": "lurking",
    "6": "cackle",
    "7": "vile",
    "8": "vampire",
    "9": "petrify",
}


def random_character_generator_start_end() -> str:
    number_of_chars = random.randrange(0, 10)
    characters = string.ascii_letters + string.punctuation
    return "".join(random.choice(characters) for i in range(number_of_chars))


def random_character_generator_middle() -> str:
    number_of_chars = random.randrange(0, 10)
    characters = list(
        string.ascii_letters + string.punctuation + string.digits
    ) + list(spooky_word.values())
    return "".join(random.choice(characters) for i in range(number_of_chars))


def create_full_encoded_line(coord: int) -> str:
    coord_str = str(coord)
    if len(coord_str) < 2:
        coord_str = "0" + coord_str
    digit_1_option = [coord_str[0], spooky_word[coord_str[0]]]
    digit_2_option = [coord_str[1], spooky_word[coord_str[1]]]
    line_options = [
        random_character_generator_start_end()
        + random.choice(digit_1_option)
        + random_character_generator_middle()
        + random.choice(digit_2_option)
        + random_character_generator_start_end(),
        random_character_generator_start_end()
        + random.choice(digit_1_option)
        + random_character_generator_start_end(),
    ]
    if coord_str[0] == coord_str[1]:
        return random.choice(line_options)
    return line_options[0]


def encode_all_coords(
    all_coords: list[tuple[int]], encode_func: Callable
) -> list[str]:
    all_coords_encoded = []
    for coord in all_coords:
        row, column = coord
        all_coords_encoded.append(encode_func(row))
        all_coords_encoded.append(encode_func(column))
    return all_coords_encoded


def write_to_file(all_lines: list[str], file_name: str):
    with open(file_name, "w") as f:
        for line in all_lines:
            f.write(f"{line}\n")


def create_input_file(
    file_to_encode: str, file_to_write_to: str, encode_func: Callable
):
    image = transform_image(file_to_encode)
    image_coords = get_coords(image)
    encoded_coords = encode_all_coords(image_coords, encode_func)
    write_to_file(encoded_coords, file_to_write_to)


if __name__ == "__main__":
    create_input_file(
        "pumpkin.txt", "matthew_wilson_input.txt", create_full_encoded_line
    )
