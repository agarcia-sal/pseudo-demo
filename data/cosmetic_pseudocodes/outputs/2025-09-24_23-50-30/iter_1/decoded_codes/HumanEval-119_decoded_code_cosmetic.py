from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        balance_value = 0
        for ch in string_to_verify:
            if ch == '(':
                balance_value += 1
            else:
                balance_value -= 1
            if balance_value < 0:
                return False
        return balance_value == 0

    combined1 = list_of_two_strings[0] + list_of_two_strings[1]
    combined2 = list_of_two_strings[1] + list_of_two_strings[0]
    result = False
    if check(combined1):
        result = True
    elif check(combined2):
        result = True
    return "Yes" if result else "No"