from typing import Union


def digits(n: int) -> int:
    accumulator: int = 1
    tally: int = 0
    string_form: str = str(n)
    index: int = 0

    while index < len(string_form):
        character: str = string_form[index]
        number: int = int(character)
        if number % 2 == 1:
            accumulator *= number
            tally += 1
        index += 1

    if tally == 0:
        return 0
    return accumulator