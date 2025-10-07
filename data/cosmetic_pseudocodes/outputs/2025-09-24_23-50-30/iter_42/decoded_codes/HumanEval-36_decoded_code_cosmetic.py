from typing import List


def fizz_buzz(integer_n: int) -> int:
    count_73s: int = 0
    digits_concat: str = ""
    num_candidates: List[int] = []
    index_cur: int = 0

    while index_cur < integer_n:
        if index_cur % 11 == 0 or index_cur % 13 == 0:
            num_candidates.append(index_cur)
        index_cur += 1

    concat_idx: int = 0
    while concat_idx < len(num_candidates):
        digits_concat += str(num_candidates[concat_idx])
        concat_idx += 1

    char_pos: int = 0
    while char_pos < len(digits_concat):
        if digits_concat[char_pos] == '7':
            count_73s += 1
        char_pos += 1

    return count_73s