from typing import Tuple

def match_parens(pair_of_strings: Tuple[str, str]) -> str:
    def validate(input_string: str) -> bool:
        counter = 0
        for current_char in input_string:
            if current_char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_string = pair_of_strings[0]
    second_string = pair_of_strings[1]

    concat_a = first_string + second_string
    concat_b = second_string + first_string

    if validate(concat_a):
        return 'Yes'
    if validate(concat_b):
        return 'Yes'
    return 'No'