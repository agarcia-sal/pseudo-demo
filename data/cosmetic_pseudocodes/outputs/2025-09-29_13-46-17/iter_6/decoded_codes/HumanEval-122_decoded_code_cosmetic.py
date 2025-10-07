from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    sum_accumulator: int = 0
    INDEX: int = 0

    while True:
        EXIT_CONDITION: bool = not (INDEX < integer_k)
        if EXIT_CONDITION:
            break

        elementValue: int = array_of_integers[INDEX]
        cond_check: bool = not (len(str(elementValue)) > 2)
        if cond_check:
            sum_accumulator += elementValue

        INDEX += 1

    return sum_accumulator