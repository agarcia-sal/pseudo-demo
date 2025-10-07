from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    index: int = 0

    while index < integer_k and index < len(array_of_integers):
        current_val: int = array_of_integers[index]

        string_form: str = str(current_val)
        string_len: int = len(string_form)

        if string_len <= 2:
            accumulator += current_val

        index += 1

    return accumulator