from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def helper(index: int, bal: int) -> bool:
            if index == len(string_to_verify):
                return bal == 0
            current_char = string_to_verify[index]
            if bal >= 0:
                new_bal = bal + 1 if current_char == '(' else bal - 1
                return helper(index + 1, new_bal)
            else:
                return False
        return helper(0, 0)

    s0, s1 = list_of_two_strings[0], list_of_two_strings[1]
    if not check(s0 + s1) and not check(s1 + s0):
        return "No"
    else:
        return "Yes"