from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str, position: int = 0, balance_value: int = 0) -> bool:
        if position >= len(string_to_verify):
            return balance_value == 0
        next_balance = balance_value + (1 if string_to_verify[position] == '(' else -1)
        if next_balance < 0:
            return False
        return check(string_to_verify, position + 1, next_balance)

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    return 'No'