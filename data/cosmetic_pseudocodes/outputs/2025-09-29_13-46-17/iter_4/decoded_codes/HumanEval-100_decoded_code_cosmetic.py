from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def pile_recursion(counter: int, accumulated: List[int]) -> List[int]:
        if counter >= positive_integer_n:
            return accumulated
        current_value = 2 * counter + positive_integer_n
        new_accumulated = accumulated + [current_value]  # append current_value immutably
        return pile_recursion(counter + 1, new_accumulated)

    return pile_recursion(0, [])