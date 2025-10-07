from typing import List

def make_a_pile(positive_integer_x: int) -> List[int]:
    resulting_list: List[int] = []
    iterator: int = 0
    while iterator < positive_integer_x:
        increment_value: int = 2 * iterator
        computed_element: int = positive_integer_x + increment_value
        resulting_list.append(computed_element)
        iterator += 1
    return resulting_list