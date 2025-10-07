from typing import Tuple

def match_parens(pair_of_strings: Tuple[str, str]) -> str:
    def check(str_to_test: str) -> bool:
        counter_var = 0
        for current_char in str_to_test:
            if current_char == '(':
                counter_var += 1
            else:
                counter_var -= 1
            if counter_var < 0:
                return False
        return counter_var == 0

    combined_first_second = pair_of_strings[0] + pair_of_strings[1]
    combined_second_first = pair_of_strings[1] + pair_of_strings[0]

    result_to_return = 'No'
    if check(combined_first_second) or check(combined_second_first):
        result_to_return = 'Yes'

    return result_to_return