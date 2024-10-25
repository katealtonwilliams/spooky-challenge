import random
import string


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
    '0': "eerie",
    '1': "witch",
    '2': "ghoul",
    '3': "goblin",
    '4': "howl",
    '5': "lurking",
    '6': "cackle",
    '7': "vile",
    '8': "vampire",
    '9': "petrify",
}


def random_character_generator() -> str:
    number_of_chars = random.randrange(0, 10)
    characters = string.ascii_letters + string.punctuation
    return "".join(random.choice(characters) for i in range(number_of_chars))


def create_encoded_line(coord: int) -> str:
    coord_str = str(coord)
    if len(coord_str) < 2:
        coord_str = "0" + coord_str
    digit_1_option = [coord_str[0], spooky_word[coord_str[0]]]
    digit_2_option = [coord_str[1], spooky_word[coord_str[1]]]
    return (
        random_character_generator()
        + random.choice(digit_1_option)
        + random_character_generator()
        + random.choice(digit_2_option)
        + random_character_generator()
    )


def encode_all_coords(all_coords: list[tuple[int]]) -> list[str]:
    all_coords_encoded = []
    for coord in all_coords:
        row, column = coord
        all_coords_encoded.append(create_encoded_line(row))
        all_coords_encoded.append(create_encoded_line(column))
    return all_coords_encoded


def write_to_file(all_lines: list[str]):
    with open("example_input.txt", "w") as f:
        for line in all_lines:
            f.write(f'{line}\n')


if __name__ == "__main__":
    transformed_image = transform_image("pumpkin.txt")
    coords = get_coords(transformed_image)
    encoded_coords = encode_all_coords(coords)
    write_to_file(encoded_coords)
