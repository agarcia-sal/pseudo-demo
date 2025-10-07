from typing import List

def circular_shift(integer_x: int, integer_shift: int) -> str:
    strVal: str = str(integer_x)
    len_val: int = len(strVal)
    char_list: List[str] = list(strVal)

    def build_reversed(curr_list: List[str], idx: int) -> str:
        if idx < 0:
            return ""
        else:
            return curr_list[idx] + build_reversed(curr_list, idx - 1)

    def compose_shifted(curr_list: List[str], n: int, shift: int) -> str:
        if n == 0 or n == shift:
            return ""
        else:
            return "".join(curr_list[n - shift : n] + curr_list[0 : n - shift])

    if not (integer_shift <= len_val):
        return build_reversed(char_list, len_val - 1)
    else:
        return compose_shifted(char_list, len_val, integer_shift)