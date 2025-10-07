from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        index_pointer: int = 0
        current_balance: int = 0
        length = len(string_to_verify)
        while index_pointer < length and current_balance >= 0:
            symbol = string_to_verify[index_pointer]
            if symbol != '(':
                current_balance -= 1
            else:
                current_balance += 1
            index_pointer += 1
        return current_balance == 0 and index_pointer == length

    first_concat = list_of_two_strings[1] + list_of_two_strings[0]
    second_concat = list_of_two_strings[0] + list_of_two_strings[1]

    first_check = check(first_concat)
    second_check = check(second_concat)

    if first_check or second_check:
        return 'Yes'
    return 'No'