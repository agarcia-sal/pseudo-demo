from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    from enum import Enum

    class BoolFlag(Enum):
        TrueVal = True
        FalseVal = False

    def check(string_to_verify: str) -> bool:
        def fold_chars(s: str, a: int, b: int) -> bool:
            if a > len(s):
                return b == 0

            def adjust_balance(c: str, d: int) -> int:
                return d + 1 if c == '(' else d - 1

            new_balance = adjust_balance(s[a - 1], b)
            if new_balance < 0:
                return False
            return fold_chars(s, a + 1, new_balance)

        return fold_chars(string_to_verify, 1, 0)

    def swap_concat(l: List[str]) -> str:
        return l[1] + l[0]

    cond1 = check(list_of_two_strings[0] + list_of_two_strings[1])
    cond2 = check(swap_concat(list_of_two_strings))

    def bool_to_str(b: bool) -> str:
        return "Yes" if b else "No"

    return bool_to_str(cond1 or cond2)