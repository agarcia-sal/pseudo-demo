from typing import Tuple

def match_parens(pair_of_strings: Tuple[str, str]) -> str:
    def validate(sequence: str) -> bool:
        counter = 0
        for current_char in sequence:
            if current_char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_concat = pair_of_strings[0] + pair_of_strings[1]
    second_concat = pair_of_strings[1] + pair_of_strings[0]
    if validate(first_concat) or validate(second_concat):
        return 'Yes'
    return 'No'