from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_input: str) -> bool:
        balance_counter = 0
        for current_char in string_input:
            if current_char == '(':
                balance_counter += 1
            else:
                balance_counter -= 1
            if balance_counter < 0:
                return False
        return balance_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return "Yes"
    else:
        return "No"