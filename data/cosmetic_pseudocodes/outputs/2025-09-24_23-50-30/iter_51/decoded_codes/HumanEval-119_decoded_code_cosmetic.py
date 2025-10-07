from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        chars = list(string_to_verify)

        def recurse(chars: List[str], index: int, acc: int) -> bool:
            if index >= len(chars):
                return acc == 0
            if acc < 0:
                return False
            delta = 2 if chars[index] == '(' else -1
            return recurse(chars, index + 1, acc + delta)

        return recurse(chars, 0, 0)

    combo_a = list_of_two_strings[0] + list_of_two_strings[1]
    combo_b = list_of_two_strings[1] + list_of_two_strings[0]

    if check(combo_a):
        return "Yes"
    if check(combo_b):
        return "Yes"
    return "No"