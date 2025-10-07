from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(parentheses_string: str) -> bool:
        balance_counter = 0
        for character in parentheses_string:
            if character == '(':
                balance_counter += 1
            else:
                balance_counter -= 1
            if balance_counter < 0:
                return False
        return balance_counter == 0

    concatenation_one = list_of_two_strings[0] + list_of_two_strings[1]
    concatenation_two = list_of_two_strings[1] + list_of_two_strings[0]

    if check(concatenation_one) or check(concatenation_two):
        return 'Yes'
    else:
        return 'No'