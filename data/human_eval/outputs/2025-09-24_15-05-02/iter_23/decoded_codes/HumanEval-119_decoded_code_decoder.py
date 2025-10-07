from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_s: str) -> bool:
        balance_value: int = 0
        for character in string_s:
            if character == '(':
                balance_value += 1
            elif character == ')':
                balance_value -= 1
            else:
                # Invalid character encountered, parentheses strings should contain only '(' or ')'.
                return False
            if balance_value < 0:
                return False
        return balance_value == 0

    if len(list_of_two_strings) != 2:
        # Invalid input length, must be exactly two strings
        return 'No'
    first_string, second_string = list_of_two_strings
    concatenation_one: str = first_string + second_string
    concatenation_two: str = second_string + first_string

    if check(concatenation_one) or check(concatenation_two):
        return 'Yes'
    else:
        return 'No'