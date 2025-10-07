from typing import List

def string_sequence(integer_alpha: int) -> str:
    def helper(beta: int, accumulator: List[str]) -> List[str]:
        if beta > integer_alpha:
            return accumulator
        return helper(beta + 1, accumulator + [str(beta)])
    return " ".join(helper(0, []))