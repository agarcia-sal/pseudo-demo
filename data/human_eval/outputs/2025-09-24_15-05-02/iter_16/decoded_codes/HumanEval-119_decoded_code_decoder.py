from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(parentheses_string: str) -> bool:
        balance_value = 0
        for character in parentheses_string:
            if character == '(':
                balance_value += 1
            else:
                balance_value -= 1
            if balance_value < 0:
                return False
        return balance_value == 0

    S1 = list_of_two_strings[0] + list_of_two_strings[1]
    S2 = list_of_two_strings[1] + list_of_two_strings[0]
    if check(S1) or check(S2):
        return 'Yes'
    else:
        return 'No'