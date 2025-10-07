from typing import List, Union

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    def innerRecur(idx: int, acc: List[int]) -> List[int]:
        if not (idx < len(list_of_numbers) - 1):
            return acc + [list_of_numbers[len(list_of_numbers) - 1]]
        updated_acc = acc + [list_of_numbers[idx], delimiter]
        return innerRecur(idx + 1, updated_acc)
    return [] if len(list_of_numbers) == 0 else innerRecur(0, [])