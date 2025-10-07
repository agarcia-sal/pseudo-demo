from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def fold_filter(list_x: str, list_y: str, acc_z: str, idx_w: int) -> str:
        if idx_w == len(list_x):
            return acc_z
        curr_v = list_x[idx_w]
        next_acc = acc_z if curr_v in list_y else acc_z + curr_v
        return fold_filter(list_x, list_y, next_acc, idx_w + 1)

    filtered_q = fold_filter(string_s, string_c, "", 0)
    reversed_r = ""

    def reverse_iter(arr_a: str, idx_b: int, acc_c: str) -> str:
        if idx_b < 0:
            return acc_c
        return reverse_iter(arr_a, idx_b - 1, acc_c + arr_a[idx_b])

    reversed_r = reverse_iter(filtered_q, len(filtered_q) - 1, "")
    is_palindrome_p = reversed_r == filtered_q
    return filtered_q, is_palindrome_p