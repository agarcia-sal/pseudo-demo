from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_s: str) -> bool:
        val: int = 0
        for char in string_s:
            if char == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
        return val == 0

    S1: str = list_of_two_strings[0] + list_of_two_strings[1]
    S2: str = list_of_two_strings[1] + list_of_two_strings[0]
    if check(S1) or check(S2):
        return 'Yes'
    return 'No'