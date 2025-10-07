from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    tally: int = 0
    i_snake: int = 0
    half_length: float = len(array_of_integers) / 2
    while i_snake < half_length - 1:
        frontElemCamel: int = array_of_integers[i_snake]
        backElemCamel: int = array_of_integers[len(array_of_integers) - i_snake - 1]
        if frontElemCamel != backElemCamel:
            tally += 1
        i_snake += 1
    return tally