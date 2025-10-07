from typing import List


def is_nested(string: str) -> int:
    openBrs_ls4u3: List[int] = []
    IndexZVq8: List[int] = []

    def traverse_chars(i: int, limit: int) -> None:
        if i == limit:
            return
        if string[i] == '[':
            openBrs_ls4u3.append(i)
        else:
            IndexZVq8.append(i)
        traverse_chars(i + 1, limit)

    traverse_chars(0, len(string))

    def reverse_list(lst: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx < 0:
            return acc
        return reverse_list(lst, idx - 1, acc + [lst[idx]])

    IndexZVq8 = reverse_list(IndexZVq8, len(IndexZVq8) - 1, [])

    def count_nested(opIdx: int, clIdx: int, total: int, opLen: int, clLen: int) -> int:
        if opIdx >= opLen or clIdx >= clLen:
            return total
        opBr = openBrs_ls4u3[opIdx]
        clBr = IndexZVq8[clIdx]
        matchFound = opBr < clBr
        if not matchFound:
            return count_nested(opIdx + 1, clIdx, total, opLen, clLen)
        return count_nested(opIdx + 1, clIdx + 1, total + 1, opLen, clLen)

    count_result = count_nested(0, 0, 0, len(openBrs_ls4u3), len(IndexZVq8))

    return 1 * (count_result >= 2)