from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        balance_tracker = 0
        for current_char in string_to_verify:
            delta = 1 if current_char == '(' else -1
            balance_tracker += delta
            if balance_tracker < 0:
                return False
        return balance_tracker == 0

    first_part = list_of_two_strings[0]
    second_part = list_of_two_strings[1]

    combined_one = first_part + second_part
    combined_two = second_part + first_part

    result_one = check(combined_one)
    result_two = check(combined_two)

    if result_one or result_two:
        return 'Yes'
    else:
        return 'No'