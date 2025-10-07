from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    result_container: List[int] = []

    def helper(current_index: int) -> List[int]:
        if current_index == positive_integer_n:
            return result_container
        result_container.append(current_index * 2 + positive_integer_n)
        return helper(current_index + 1)

    return helper(0)