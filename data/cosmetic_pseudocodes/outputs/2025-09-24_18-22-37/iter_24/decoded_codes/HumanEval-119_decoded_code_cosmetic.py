from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        delta: int = 0
        for ch in string_to_verify:
            if ch == '(':
                delta += 1
            else:
                delta -= 1

            if delta < 0:
                return False
        return delta == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    valid_check_first = check(first_concat)
    valid_check_second = check(second_concat)

    if valid_check_first or valid_check_second:
        return 'Yes'
    return 'No'