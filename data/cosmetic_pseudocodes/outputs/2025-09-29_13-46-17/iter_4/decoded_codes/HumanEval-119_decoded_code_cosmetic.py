from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def verify_balance(target_string: str) -> bool:
        balance_count: int = 0
        index_counter: int = 0

        def recurse_chars() -> bool:
            nonlocal balance_count, index_counter
            if index_counter == len(target_string):
                return balance_count == 0
            current_char = target_string[index_counter]
            if current_char != '(':
                balance_count -= 1
            else:
                balance_count += 1
            if balance_count < 0:
                return False
            index_counter += 1
            return recurse_chars()

        return recurse_chars()

    combo_a = list_of_two_strings[0] + list_of_two_strings[1]
    combo_b = list_of_two_strings[1] + list_of_two_strings[0]

    if not verify_balance(combo_b) and not verify_balance(combo_a):
        return "No"
    return "Yes"