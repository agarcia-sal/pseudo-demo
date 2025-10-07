from typing import Union

def digits(n: Union[int, str]) -> int:
    result: int = 1
    tally: int = 0
    n_str: str = str(n)
    for index in range(len(n_str)):
        current_char: str = n_str[index]
        number: int = int(current_char)
        if number % 2 != 0:
            result *= number
            tally += 1
    return result if tally != 0 else 0