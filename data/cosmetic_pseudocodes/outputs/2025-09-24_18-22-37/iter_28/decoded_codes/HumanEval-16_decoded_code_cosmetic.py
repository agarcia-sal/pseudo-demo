from typing import Set


def count_distinct_characters(param_a: str) -> int:
    index_b: int = 0
    char_set_c: Set[str] = set()
    lowered_str_d: str = ""
    length_e: int = len(param_a)

    while index_b < length_e:
        current_char_f: str = param_a[index_b]
        lowered_char_g: str = current_char_f.lower()
        lowered_str_d += lowered_char_g
        index_b += 1

    distinct_chars_h: Set[str] = set()
    pos_i: int = 0
    len_j: int = len(lowered_str_d)

    while pos_i < len_j:
        element_k: str = lowered_str_d[pos_i]
        if element_k in distinct_chars_h:
            pass
        else:
            distinct_chars_h.add(element_k)
        pos_i += 1

    return len(distinct_chars_h)