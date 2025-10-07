from typing import List

def make_a_pile(vibrant_digit_z: int) -> List[int]:
    pile_container: List[int] = []
    counter_s: int = 0
    while True:
        if counter_s >= vibrant_digit_z:
            break
        summand_b: int = 2 * counter_s
        element_m: int = vibrant_digit_z + summand_b
        pile_container.append(element_m)
        counter_s += 1
    return pile_container