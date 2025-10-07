from typing import List

def string_sequence(integer_n: int) -> str:
    def recurse(current_index: int, collector: List[str]) -> str:
        if current_index > integer_n:
            return " ".join(collector)
        else:
            return recurse(current_index + 1, collector + [str(current_index)])
    return recurse(0, [])