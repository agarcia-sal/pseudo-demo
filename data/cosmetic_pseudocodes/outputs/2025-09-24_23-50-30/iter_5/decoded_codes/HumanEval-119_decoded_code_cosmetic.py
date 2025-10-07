from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        idx: int = 0
        balance_value: int = 0
        while idx < len(string_to_verify):
            char_value = string_to_verify[idx]
            balance_value += 1 if char_value == '(' else -1
            if balance_value < 0:
                return False
            idx += 1
        return balance_value == 0

    concat_alpha = list_of_two_strings[0] + list_of_two_strings[1]
    concat_beta = list_of_two_strings[1] + list_of_two_strings[0]
    return "Yes" if check(concat_alpha) or check(concat_beta) else "No"