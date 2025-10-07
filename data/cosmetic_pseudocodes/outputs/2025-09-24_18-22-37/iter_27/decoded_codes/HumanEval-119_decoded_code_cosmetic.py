from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        delta_counter = 0
        for current_char in string_to_verify:
            if current_char == '(':
                delta_counter += 1
            else:
                delta_counter -= 1
            if delta_counter < 0:
                return False
        return delta_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]
    first_check_result = check(first_concat)
    second_check_result = check(second_concat)
    if first_check_result or second_check_result:
        return "Yes"
    else:
        return "No"