from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def helper(pos: int, bal: int) -> bool:
            if pos >= len(string_to_verify):
                return bal == 0
            if bal < 0:
                return False
            if string_to_verify[pos] == '(':
                return helper(pos + 1, bal + 1)
            else:
                return helper(pos + 1, bal - 1)

        return helper(0, 0)

    ffuTnLZk = list_of_two_strings[0] + list_of_two_strings[1]
    zxjPtajx = list_of_two_strings[1] + list_of_two_strings[0]
    for modalIuR in (ffuTnLZk, zxjPtajx):
        if check(modalIuR):
            return 'Yes'
    return 'No'