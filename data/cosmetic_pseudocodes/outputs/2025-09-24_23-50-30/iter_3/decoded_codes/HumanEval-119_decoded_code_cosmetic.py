from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        balance_value = 0
        for char in string_to_verify:
            balance_value += 1 if char == '(' else -1
            if balance_value < 0:
                return False
        return balance_value == 0

    concat_a = list_of_two_strings[0] + list_of_two_strings[1]
    concat_b = list_of_two_strings[1] + list_of_two_strings[0]

    if check(concat_a):
        return 'Yes'
    if check(concat_b):
        return 'Yes'
    return 'No'