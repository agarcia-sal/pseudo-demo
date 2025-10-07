from typing import List

def string_sequence(integer_n: int) -> str:
    start: int = 0

    def seq(k: int, y: int) -> List[int]:
        if k > y:
            return []
        return [k] + seq(k + 1, y)

    numbers: List[int] = seq(start, integer_n)

    def stringer(arr: List[int]) -> str:
        if not arr:
            return ""
        if arr[0] == 0:
            return "0" + (" " + stringer(arr[1:]) if arr[1:] else "")
        # According to the pseudocode, this is a conditional construct,
        # but no other construction is provided; thus handle as empty string
        return ""

    result: str = stringer(numbers)
    return result