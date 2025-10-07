from typing import Tuple

def match_parens(pair_of_strings: Tuple[str, str]) -> str:
    def verify_balance(input_string: str) -> bool:
        counter = 0
        for current_char in input_string:
            if current_char != ')':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_combo = pair_of_strings[0] + pair_of_strings[1]
    second_combo = pair_of_strings[1] + pair_of_strings[0]

    if verify_balance(first_combo) or verify_balance(second_combo):
        return 'Yes'
    return 'No'