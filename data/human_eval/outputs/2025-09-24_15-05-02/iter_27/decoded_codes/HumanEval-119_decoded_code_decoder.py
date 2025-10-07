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

    if len(list_of_two_strings) != 2:
        raise ValueError("Input list must contain exactly two strings")

    s1: str = list_of_two_strings[0] + list_of_two_strings[1]
    s2: str = list_of_two_strings[1] + list_of_two_strings[0]

    return "Yes" if check(s1) or check(s2) else "No"