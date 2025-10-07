from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter_var = 0
        idx_tracker = 0
        while idx_tracker < len(string_to_verify):
            current_char = string_to_verify[idx_tracker]
            if current_char == '(':
                counter_var += 1
            else:
                counter_var -= 1
            if counter_var < 0:
                return False
            idx_tracker += 1
        return counter_var == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]
    if check(first_concat):
        return 'Yes'
    elif check(second_concat):
        return 'Yes'
    return 'No'