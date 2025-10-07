from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_alpha: str) -> bool:
        idx_counter = 0
        acc_balance = 0

        while idx_counter < len(string_alpha):
            current_ch = string_alpha[idx_counter]

            if current_ch == '(':
                acc_balance += 1
            elif current_ch == ')':
                acc_balance -= 1

            if acc_balance < 0:
                return False

            idx_counter += 1

        return acc_balance == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    else:
        return 'No'