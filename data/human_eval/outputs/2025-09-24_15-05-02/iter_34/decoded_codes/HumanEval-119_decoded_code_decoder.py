from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        balance_value = 0
        for character in string_to_verify:
            if character == '(':
                balance_value += 1
            else:
                balance_value -= 1
            if balance_value < 0:
                return False
        return balance_value == 0

    concatenation_one = list_of_two_strings[0] + list_of_two_strings[1]
    concatenation_two = list_of_two_strings[1] + list_of_two_strings[0]
    if check(concatenation_one) or check(concatenation_two):
        return 'Yes'
    else:
        return 'No'