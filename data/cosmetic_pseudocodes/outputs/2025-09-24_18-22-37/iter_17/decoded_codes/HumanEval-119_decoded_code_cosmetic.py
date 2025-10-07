from typing import List

def match_parens(pairs_array: List[str]) -> str:
    def verify_balance(candidate_string: str) -> bool:
        counter = 0
        idx = 0
        length = len(candidate_string)
        while idx < length:
            current_char = candidate_string[idx]
            idx += 1
            if current_char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    combo_a = pairs_array[0] + pairs_array[1]
    combo_b = pairs_array[1] + pairs_array[0]
    if verify_balance(combo_a):
        return "Yes"
    elif verify_balance(combo_b):
        return "Yes"
    else:
        return "No"