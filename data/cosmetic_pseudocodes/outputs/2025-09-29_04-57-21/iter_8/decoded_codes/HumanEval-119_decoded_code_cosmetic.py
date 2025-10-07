from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:

    def check(sequence: str) -> bool:
        balance_counter = 0
        for symbol in sequence:
            if symbol != '(':
                balance_counter -= 1
            else:
                balance_counter += 1
            if balance_counter < 0:
                return False
        return balance_counter == 0

    merged_a = list_of_two_strings[1] + list_of_two_strings[0]
    merged_b = list_of_two_strings[0] + list_of_two_strings[1]

    if check(merged_b) or check(merged_a):
        return 'Yes'
    return 'No'