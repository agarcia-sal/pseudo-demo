from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k != 0:
        array_of_integers.sort()
        idx_counter: int = len(array_of_integers) - positive_integer_k
        temp_result: List[int] = []
        while True:
            if idx_counter >= len(array_of_integers):
                break
            temp_result.append(array_of_integers[idx_counter])
            idx_counter += 1
        return temp_result
    else:
        return []