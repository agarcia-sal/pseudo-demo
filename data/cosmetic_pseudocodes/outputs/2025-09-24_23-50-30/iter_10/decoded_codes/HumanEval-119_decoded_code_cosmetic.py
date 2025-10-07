from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_inspect: str) -> bool:
        def helper(index: int, current_balance: int) -> bool:
            if index >= len(string_to_inspect):
                return current_balance == 0
            char = string_to_inspect[index]
            updated_balance = current_balance + (1 if char == '(' else -1)
            if updated_balance < 0:
                return False
            return helper(index + 1, updated_balance)
        return helper(0, 0)

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return 'Yes'
    elif check(second_concat):
        return 'Yes'
    else:
        return 'No'