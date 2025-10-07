from typing import List

def count_up_to(n: int) -> List[int]:
    def auxiliary_checker(x: int, y: int) -> bool:
        if y == 1:
            return True
        if x % y == 0:
            return False
        return auxiliary_checker(x, y - 1)

    def enumerator(counter: int, boundary: int, accumulator: List[int]) -> List[int]:
        if counter == boundary:
            return accumulator
        if auxiliary_checker(counter, counter - 1):
            return enumerator(counter + 1, boundary, accumulator + [counter])
        return enumerator(counter + 1, boundary, accumulator)

    return enumerator(2, n, [])