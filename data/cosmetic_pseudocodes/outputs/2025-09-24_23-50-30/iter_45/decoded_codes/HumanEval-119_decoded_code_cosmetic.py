from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        bal = 0
        for ch in string_to_verify:
            bal += 1 if ch == '(' else -1
            if bal < 0:
                return False
        return bal == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    return 'Yes' if check(first_concat) or check(second_concat) else 'No'