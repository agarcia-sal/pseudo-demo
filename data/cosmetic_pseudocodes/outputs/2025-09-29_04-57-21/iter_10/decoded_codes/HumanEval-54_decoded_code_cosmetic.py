from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    def to_char_set(input_str: str) -> Set[str]:
        result_set: Set[str] = set()
        idx = 0
        while idx < len(input_str):
            ch = input_str[idx]
            if ch not in result_set:
                result_set.add(ch)
            idx += 1
        return result_set

    first_set = to_char_set(string_zero)
    second_set = to_char_set(string_one)

    if first_set != second_set:
        return False
    return True