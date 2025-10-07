from typing import Sequence

def match_parens(arr_pair: Sequence[str]) -> str:
    def check(validate_str: str) -> bool:
        counter_accum = 0
        idx_ptr = 0
        length = len(validate_str)
        while idx_ptr < length:
            curr_char = validate_str[idx_ptr]
            if curr_char == '(':
                counter_accum += 1
            else:
                counter_accum -= 1
            if counter_accum < 0:
                return False
            idx_ptr += 1
        return counter_accum == 0

    first_junc = arr_pair[0]
    second_junc = arr_pair[1]
    combo_a = first_junc + second_junc
    combo_b = second_junc + first_junc
    is_valid_a = check(combo_a)
    is_valid_b = check(combo_b)

    if is_valid_a or is_valid_b:
        return 'Yes'
    return 'No'