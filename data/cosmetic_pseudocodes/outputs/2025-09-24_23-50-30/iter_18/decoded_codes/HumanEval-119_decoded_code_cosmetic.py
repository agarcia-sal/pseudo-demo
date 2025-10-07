from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        balance_value = 0
        for current_char in string_to_verify:
            if current_char != '(':
                balance_value -= 1
            else:
                balance_value += 1
            if balance_value < 0:
                return False
        return balance_value == 0

    part_a = list_of_two_strings[0]
    part_b = list_of_two_strings[1]
    if check(part_a + part_b):
        return 'Yes'
    if check(part_b + part_a):
        return 'Yes'
    return 'No'