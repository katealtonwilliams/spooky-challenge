import random
import string
from create_full_input import create_input_file, spooky_word


def random_generator_1():
    number_chars = random.randrange(0, 5)
    characters = string.ascii_letters
    return "".join(random.choice(characters) for i in range(number_chars))


def random_generator_2():
    number_chars = random.randrange(0, 5)
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(number_chars))


def random_generator_3() -> str:
    number_of_chars = random.randrange(0, 5)
    characters = list(string.ascii_letters + string.punctuation + string.digits) + list(
        spooky_word.values()
    )
    return "".join(random.choice(characters) for i in range(number_of_chars))


def encode_line_example_1(coord: int) -> str:
    coord_str = str(coord)
    if len(coord_str) < 2:
        coord_str = "0" + coord_str
    return (
        random_generator_1()
        + coord_str[0]
        + random_generator_2()
        + coord_str[1]
        + random_generator_1()
    )


def encode_line_example_2(coord: int) -> str:
    coord_str = str(coord)
    if len(coord_str) < 2:
        coord_str = "0" + coord_str
    digit_1_option = [coord_str[0], spooky_word[coord_str[0]]]
    digit_2_option = [coord_str[1], spooky_word[coord_str[1]]]
    return (
        random_generator_1()
        + random.choice(digit_1_option)
        + random_generator_2()
        + random.choice(digit_2_option)
        + random_generator_1()
    )


def encode_line_example_3(coord: int) -> str:
    coord_str = str(coord)
    if len(coord_str) < 2:
        coord_str = "0" + coord_str
    digit_1_option = [coord_str[0], spooky_word[coord_str[0]]]
    digit_2_option = [coord_str[1], spooky_word[coord_str[1]]]
    return (
        random_generator_1()
        + random.choice(digit_1_option)
        + random_generator_3()
        + random.choice(digit_2_option)
        + random_generator_1()
    )


if __name__ == "__main__":
    create_input_file(
        "example_picture_1.txt", "example_1_input.txt", encode_line_example_1
    )
    create_input_file(
        "example_picture_2.txt", "example_2_input.txt", encode_line_example_2
    )
    create_input_file(
        "example_picture_3.txt", "example_3_input.txt", encode_line_example_3
    )
