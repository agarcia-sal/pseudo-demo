from typing import List

def match_parens(input_array: List[str]) -> str:
    def check(current_string: str) -> bool:
        accum: int = 0
        for ch in current_string:
            if ch == '(':
                accum += 1
            else:
                accum -= 1
            if accum < 0:
                return False
        return accum == 0

    first_concat = input_array[0] + input_array[1]
    second_concat = input_array[1] + input_array[0]

    if check(first_concat):
        return "Yes"
    elif check(second_concat):
        return "Yes"
    else:
        return "No"