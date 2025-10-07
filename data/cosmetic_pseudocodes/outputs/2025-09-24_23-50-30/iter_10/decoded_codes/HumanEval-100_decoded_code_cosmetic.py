from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    def helper(counter: int, accumulator: List[int]) -> List[int]:
        if counter == positive_integer_n:
            return accumulator
        # The 'new_value' calculation is unused; preserved from pseudocode but skipped in result
        _new_value = counter << 1 + positive_integer_n - positive_integer_n + positive_integer_n + counter
        return helper(counter + 1, accumulator + [positive_integer_n + (counter << 1)])

    return helper(0, [])