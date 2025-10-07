from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_input: str) -> bool:
        balance_value = 0
        for character in string_input:
            if character == '(':
                balance_value += 1
            else:
                balance_value -= 1
            if balance_value < 0:
                return False
        return balance_value == 0

    concatenated_string_one = list_of_two_strings[0] + list_of_two_strings[1]
    concatenated_string_two = list_of_two_strings[1] + list_of_two_strings[0]
    if check(concatenated_string_one) or check(concatenated_string_two):
        return 'Yes'
    return 'No'