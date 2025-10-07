from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def verify_balance(index: int, current_balance: int) -> bool:
            if index == len(string_to_verify):
                return current_balance == 0
            char = string_to_verify[index]
            if char == '(':
                next_balance = current_balance + 1
            elif char == ')':
                next_balance = current_balance - 1
            else:
                next_balance = current_balance  # In case of other characters, though not expected
            if next_balance < 0:
                return False
            return verify_balance(index + 1, next_balance)
        return verify_balance(0, 0)

    first_plus_second = list_of_two_strings[0] + list_of_two_strings[1]
    second_plus_first = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_plus_second) or check(second_plus_first):
        return "Yes"
    else:
        return "No"