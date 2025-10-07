from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string: str) -> bool:
        balance_counter = 0
        for char in string:
            if char == '(':
                balance_counter += 1
            else:
                balance_counter -= 1
            if balance_counter < 0:
                return False
        return balance_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'