from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def balance_index(index_value: int, current_balance: int) -> bool:
            if index_value > len(string_to_verify):
                return current_balance == 0
            char = string_to_verify[index_value - 1]  # Adjust for 1-based logic in pseudocode
            new_balance = current_balance + 1 if char == '(' else current_balance - 1
            if new_balance < 0:
                return False
            return balance_index(index_value + 1, new_balance)
        return balance_index(1, 0)

    combined_first = list_of_two_strings[0] + list_of_two_strings[1]
    combined_second = list_of_two_strings[1] + list_of_two_strings[0]

    if check(combined_first) or check(combined_second):
        result = 'Yes'
    else:
        result = 'No'
    return result