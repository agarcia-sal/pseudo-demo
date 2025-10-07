from typing import Union

def digits(x: Union[int, float, str]) -> int:
    accumulation: int = 1
    tally: int = 0
    for element in str(x):
        try:
            num = int(element)
        except ValueError:
            continue  # skip non-digit characters
        if num % 2 == 1:
            accumulation *= num
            tally += 1
    return 0 if tally == 0 else accumulation