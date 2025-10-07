from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def recurse(index: int, total: int) -> int:
        if index > integer_k or index > len(array_of_integers):
            return total
        current_val = array_of_integers[index - 1]
        str_len = len(str(current_val))
        if str_len <= 2:
            total += current_val
        return recurse(index + 1, total)
    return recurse(1, 0)