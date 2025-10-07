from typing import List

def make_a_pile(number_of_elements: int) -> List[int]:
    result: List[int] = []
    counter: int = 0
    while counter < number_of_elements:
        result.append(counter * 2 + number_of_elements)
        counter += 1
    return result