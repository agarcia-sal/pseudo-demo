from typing import Tuple

def match_parens(input_pair: Tuple[str, str]) -> str:
    def check(inner_string: str) -> bool:
        counter: int = 0
        for char in inner_string:
            if char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_concat = input_pair[0] + input_pair[1]
    second_concat = input_pair[1] + input_pair[0]
    result_flag = False

    if check(first_concat):
        result_flag = True
    elif check(second_concat):
        result_flag = True
    else:
        result_flag = False

    return 'Yes' if result_flag else 'No'