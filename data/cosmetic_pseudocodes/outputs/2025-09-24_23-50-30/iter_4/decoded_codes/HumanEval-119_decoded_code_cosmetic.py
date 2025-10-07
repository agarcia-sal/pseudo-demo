from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def helper(index: int, count: int) -> bool:
            if index == len(string_to_verify):
                return count == 0
            if count < 0:
                return False
            delta = 1 if string_to_verify[index] == '(' else -1
            return helper(index + 1, count + delta)
        return helper(0, 0)

    s1, s2 = list_of_two_strings
    combined_variants = [s1 + s2, s2 + s1]
    return 'Yes' if any(check(x) for x in combined_variants) else 'No'