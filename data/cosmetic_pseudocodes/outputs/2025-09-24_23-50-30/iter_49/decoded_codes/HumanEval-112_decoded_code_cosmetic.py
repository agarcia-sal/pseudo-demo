from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_and_build(input_p: str, filter_q: str, output_r: str) -> str:
        if not input_p:
            return output_r
        head, tail = input_p[0], input_p[1:]
        if head not in filter_q:
            return filter_and_build(tail, filter_q, output_r + head)
        else:
            return filter_and_build(tail, filter_q, output_r)

    cleaned_v = filter_and_build(string_s, string_c, "")

    def is_palindrome_check(seq_x: str, idx_y: int, idx_z: int) -> bool:
        if idx_y >= idx_z:
            return True
        if seq_x[idx_y] != seq_x[idx_z]:
            return False
        return is_palindrome_check(seq_x, idx_y + 1, idx_z - 1)

    return cleaned_v, is_palindrome_check(cleaned_v, 0, len(cleaned_v) - 1)