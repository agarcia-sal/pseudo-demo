from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(str_param: str) -> bool:
        def recur(idx: int, bal: int) -> bool:
            if idx >= len(str_param):
                return bal == 0
            if bal < 0:
                return False
            curr_char = str_param[idx]
            new_bal = bal + (2 if curr_char == '(' else -1)
            return recur(idx + 1, new_bal)
        return recur(0, 0)

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    return 'No'