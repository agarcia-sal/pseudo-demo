from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter_value = 0
        for current_char in string_to_verify:
            is_open_paren = current_char == '('
            increment_amount = 2 * is_open_paren - 1  # +1 if '(', else -1
            counter_value += increment_amount
            if counter_value < 0:
                return False
        return counter_value == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'