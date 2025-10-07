from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        current_balance = 0
        for current_char in string_to_verify:
            if current_char == '(':
                current_balance += 1
            else:
                current_balance -= 1
            if current_balance < 0:
                return False
        return current_balance == 0

    combined_a = list_of_two_strings[0] + list_of_two_strings[1]
    combined_b = list_of_two_strings[1] + list_of_two_strings[0]

    if check(combined_a):
        return "Yes"
    if check(combined_b):
        return "Yes"
    return "No"