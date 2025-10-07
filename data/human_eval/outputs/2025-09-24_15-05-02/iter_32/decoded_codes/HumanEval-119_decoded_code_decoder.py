from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_sequence: str) -> bool:
        balance_value = 0
        for character in string_sequence:
            if character == '(':
                balance_value += 1
            else:
                balance_value -= 1
            if balance_value < 0:
                return False
        return balance_value == 0

    first_concatenation = list_of_two_strings[0] + list_of_two_strings[1]
    second_concatenation = list_of_two_strings[1] + list_of_two_strings[0]
    if check(first_concatenation) or check(second_concatenation):
        return 'Yes'
    else:
        return 'No'