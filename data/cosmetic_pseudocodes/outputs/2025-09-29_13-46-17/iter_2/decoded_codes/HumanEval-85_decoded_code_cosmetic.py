from typing import List


def add(list_of_integers: List[int]) -> int:
    def helper(index: int, acc: int) -> int:
        if index >= len(list_of_integers):
            return acc
        current_value = list_of_integers[index]
        updated_acc = acc + current_value if current_value % 2 == 0 else acc
        return helper(index + 2, updated_acc)

    return helper(1, 0)