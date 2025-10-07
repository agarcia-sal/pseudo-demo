from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    result_container: List[int] = []
    counter: int = 0

    while counter < positive_integer_n:
        computed_element: int = positive_integer_n + (counter * 2)
        result_container.append(computed_element)
        counter += 1

    return result_container