from typing import List

def add(list_of_integers: List[int]) -> int:
    def helper(index: int, acc: int) -> int:
        if index > len(list_of_integers):
            return acc
        elif list_of_integers[index - 1] % 2 == 0:
            return helper(index + 2, acc + list_of_integers[index - 1])
        else:
            return helper(index + 2, acc)
    return helper(1, 0)