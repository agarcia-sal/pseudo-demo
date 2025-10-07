from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        temp_balance = 0
        for current_symbol in string_to_verify:
            if current_symbol == '(':
                temp_balance += 1
            else:
                temp_balance -= 1
            if temp_balance < 0:
                return False
        return temp_balance == 0

    first_concat = list_of_two_strings[1] + list_of_two_strings[0]
    second_concat = list_of_two_strings[0] + list_of_two_strings[1]
    if check(second_concat):
        return 'Yes'
    if check(first_concat):
        return 'Yes'
    return 'No'