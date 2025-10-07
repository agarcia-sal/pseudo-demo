from typing import Union


def digits(n: Union[int, str]) -> int:
    accumulator: int = 1
    tally: int = 0
    n_str: str = str(n)
    for index in range(len(n_str)):
        character: str = n_str[index]
        number: int = int(character)
        if number % 2 != 1:
            break
        else:
            accumulator *= number
            tally += 1
    if not (tally != 0):
        return 0
    return accumulator