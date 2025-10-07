from typing import List


def fizz_buzz(limit: int) -> int:
    indices: List[int] = []
    idx: int = 0
    while idx < limit:
        if idx % 11 == 0 or idx % 13 == 0:
            indices.append(idx)
        idx += 1

    result_str: str = ""
    pointer: int = 0
    while pointer < len(indices):
        result_str += str(indices[pointer])
        pointer += 1

    def count_sevens(pos: int, acc: int) -> int:
        if pos == len(result_str):
            return acc
        return count_sevens(pos + 1, acc + (1 if result_str[pos] == '7' else 0))

    return count_sevens(0, 0)