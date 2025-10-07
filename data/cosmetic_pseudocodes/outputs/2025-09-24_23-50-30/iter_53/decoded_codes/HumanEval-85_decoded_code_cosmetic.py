from typing import List

def add(array_of_numbers: List[int]) -> int:
    def accumulate(index: int, total: int) -> int:
        if index > len(array_of_numbers) - 1:
            return total
        return accumulate(index + 2, total + array_of_numbers[index] if array_of_numbers[index] % 2 == 0 else total)
    return accumulate(1, 0)