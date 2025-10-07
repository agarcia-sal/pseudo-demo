from typing import List, Tuple

def match_parens(array_of_dual_elements: List[Tuple[str, str]]) -> str:
    def check(sequence: Tuple[str, ...]) -> bool:
        def recur(index: int, tally: int) -> bool:
            if index >= len(sequence):
                return tally == 0
            delta = 1 if sequence[index] == '(' else -1
            if tally + delta < 0:
                return False
            return recur(index + 1, tally + delta)
        return recur(0, 0)

    first_combined = array_of_dual_elements[0] + array_of_dual_elements[1]
    second_combined = array_of_dual_elements[1] + array_of_dual_elements[0]
    return "Yes" if check(first_combined) or check(second_combined) else "No"