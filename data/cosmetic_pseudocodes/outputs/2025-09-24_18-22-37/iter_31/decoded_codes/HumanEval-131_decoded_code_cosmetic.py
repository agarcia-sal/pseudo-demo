from typing import Union

def digits(x: Union[int, float]) -> int:
    accumulator: int = 1
    tally: int = 0
    string_form: str = str(x)
    idx: int = 0
    while idx < len(string_form):
        char: str = string_form[idx]
        if char.isdigit():
            num_value: int = int(char)
            if num_value % 2 != 0:
                accumulator *= num_value
                tally += 1
        idx += 1
    return 0 if tally == 0 else accumulator