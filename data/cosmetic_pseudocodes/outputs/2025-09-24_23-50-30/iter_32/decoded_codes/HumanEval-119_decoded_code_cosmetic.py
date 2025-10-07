from typing import Tuple


def match_parens(input_pair: Tuple[str, str]) -> str:
    def check(input_str: str) -> bool:
        counter = 0
        for char in input_str:
            if char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_concat = input_pair[0] + input_pair[1]
    second_concat = input_pair[1] + input_pair[0]

    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'