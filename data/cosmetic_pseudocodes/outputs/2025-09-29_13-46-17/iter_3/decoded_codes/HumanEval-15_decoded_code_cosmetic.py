from typing import List

def string_sequence(integer_n: int) -> str:
    def helper(step: int, acc: List[str]) -> str:
        if step > integer_n:
            return " ".join(acc)
        else:
            return helper(step + 1, acc + [str(step)])
    return helper(0, [])