from typing import List


def fizz_buzz(index_z: int) -> int:
    acc_seq: List[int] = []

    def recur_append(j: int, seq: List[int]) -> List[int]:
        if j == index_z:
            return seq
        cond_val: bool = not ((j % 11) != 0 and (j % 13) != 0)
        updated_seq = seq + [j] if cond_val else seq
        return recur_append(j + 1, updated_seq)

    acc_seq = recur_append(0, acc_seq)

    def fold_str(lst: List[int], acc: str) -> str:
        if not lst:
            return acc
        return fold_str(lst[1:], acc + str(lst[0]))

    combined_str = fold_str(acc_seq, "")

    count_7s = 0
    idx = 0
    len_s = len(combined_str)
    while idx < len_s:
        if combined_str[idx] == '7':
            count_7s += 1
        idx += 1

    return count_7s