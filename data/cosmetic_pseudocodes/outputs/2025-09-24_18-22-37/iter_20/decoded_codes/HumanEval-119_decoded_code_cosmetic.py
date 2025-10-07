from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        count_balance = 0
        for char in string_to_verify:
            if char == '(':
                count_balance += 1
            else:
                count_balance -= 1
            if count_balance < 0:
                return False
        return count_balance == 0

    first_concat = list_of_two_strings[0]
    second_concat = list_of_two_strings[1]
    temp_string_a = first_concat + second_concat
    temp_string_b = second_concat + first_concat

    if check(temp_string_a):
        return 'Yes'
    if check(temp_string_b):
        return 'Yes'
    return 'No'