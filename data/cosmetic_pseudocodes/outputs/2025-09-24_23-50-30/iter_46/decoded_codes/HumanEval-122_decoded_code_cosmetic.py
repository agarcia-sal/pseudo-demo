from typing import List


def add_elements(data_list: List[int], limit: int) -> int:
    def helper(index: int, acc: int) -> int:
        if index >= limit:
            return acc
        if len(str(data_list[index])) <= 2:
            return helper(index + 1, acc + data_list[index])
        return helper(index + 1, acc)

    return helper(0, 0)