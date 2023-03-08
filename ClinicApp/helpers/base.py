import random

def random_string_generator(
        length: int = 10,
        digits: bool = True,
        alphabets: bool = False,
        special_characters:bool = False
) -> str:
    string = ""
    if digits:
        string += "01234567890"
    if alphabets:
        string += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if special_characters:
        string += "!@#$%^&*"
    return "".join([random.choice(string) for char in range(length)])
