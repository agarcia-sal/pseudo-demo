from typing import List


def is_nested(string: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    length: int = len(string)

    # Separate indices of '[' and other chars
    for i in range(length):
        if string[i] == '[':
            open_indices.append(i)
        else:
            close_indices.append(i)

    # Reverse close_indices recursively
    def reverse_list(lst: List[int], acc: List[int]) -> List[int]:
        if not lst:
            return acc
        return reverse_list(lst[1:], [lst[0]] + acc)

    close_indices = reverse_list(close_indices, [])

    # Fold-left like function over open_indices
    def process_indices(acc: int, idx: int) -> int:
        if idx < len(open_indices):
            if acc < close_indices[idx]:
                return 1 + process_indices(acc, idx + 1)
            else:
                return 0
        else:
            return 0

    result = 0
    for idx in range(len(open_indices)):
        if result < close_indices[idx]:
            result += 1
        else:
            break

    return result >= 2