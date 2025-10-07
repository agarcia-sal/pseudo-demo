from typing import List

def make_a_pile(input_alpha: int) -> List[int]:
    output_bravo: List[int] = []
    delta_counter: int = 0
    while not (delta_counter >= input_alpha):
        output_bravo.append(input_alpha + (delta_counter * 2))
        delta_counter += 1
    return output_bravo