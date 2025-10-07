from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_check: str) -> bool:
        balance_counter = 0
        for character in string_to_check:
            if character == '(':
                balance_counter += 1
            else:
                balance_counter -= 1
            if balance_counter < 0:
                return False
        return balance_counter == 0

    first_concatenation = list_of_two_strings[0] + list_of_two_strings[1]
    second_concatenation = list_of_two_strings[1] + list_of_two_strings[0]
    return 'Yes' if check(first_concatenation) or check(second_concatenation) else 'No'