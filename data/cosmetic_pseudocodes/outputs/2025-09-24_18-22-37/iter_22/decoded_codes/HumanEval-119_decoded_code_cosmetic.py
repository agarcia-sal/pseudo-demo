from typing import Tuple

def match_parens(input_pair: Tuple[str, str]) -> str:
    def verify(candidate_string: str) -> bool:
        counter = 0
        for current_char in candidate_string:
            if current_char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_concat = input_pair[0] + input_pair[1]
    second_concat = input_pair[1] + input_pair[0]
    if verify(first_concat) or verify(second_concat):
        return 'Yes'
    else:
        return 'No'