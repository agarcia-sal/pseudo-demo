from typing import List

def match_parens(two_strings_list: List[str]) -> str:
    def check(to_validate_string: str) -> bool:
        bal = 0
        idx = 0
        while idx < len(to_validate_string):
            ch = to_validate_string[idx]
            if ch == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
            idx += 1
        return bal == 0

    first_combination = two_strings_list[0] + two_strings_list[1]
    second_combination = two_strings_list[1] + two_strings_list[0]

    if check(first_combination):
        return 'Yes'
    if check(second_combination):
        return 'Yes'
    return 'No'