from typing import Tuple

def match_parens(pair_of_strings: Tuple[str, str]) -> str:
    def validate(expression: str) -> bool:
        counter: int = 0
        idx: int = 0

        while idx < len(expression):
            current_char = expression[idx]

            if current_char == '(':
                counter += 1
            else:
                # Assume character to be ')'
                counter -= 1

            if counter < 0:
                return False

            idx += 1

        return counter == 0

    merged_a = pair_of_strings[0] + pair_of_strings[1]
    merged_b = pair_of_strings[1] + pair_of_strings[0]

    if validate(merged_a) or validate(merged_b):
        return 'Yes'
    else:
        return 'No'