from typing import List

def string_sequence(integer_n: int) -> str:
    def helper(current: int, end: int, acc: List[str]) -> List[str]:
        if current > end:
            return acc
        return helper(current + 1, end, acc + [str(current)])

    result: List[str] = helper(0, integer_n, [])
    return " ".join(result)