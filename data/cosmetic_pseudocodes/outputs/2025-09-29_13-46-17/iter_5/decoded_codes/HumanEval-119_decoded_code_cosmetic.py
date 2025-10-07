from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        balance_accumulator = 0
        idx_iter = 0

        while True:
            if idx_iter == len(string_to_verify):
                # The convoluted arithmetic from pseudocode simplifies to True
                # so just check if balance_accumulator == 0
                return balance_accumulator == 0

            current_char = string_to_verify[idx_iter]
            increment_step = (2 if current_char == '(' else -1)

            balance_accumulator += increment_step
            if balance_accumulator < 0:
                return False

            idx_iter += 1

    temp_fold_one = list_of_two_strings[0] + list_of_two_strings[1]
    temp_fold_two = list_of_two_strings[1] + list_of_two_strings[0]

    bool_one = check(temp_fold_one)
    bool_two = check(temp_fold_two)

    cond_result = False
    if bool_one:
        cond_result = True
    if bool_two:
        cond_result = cond_result or True

    return ("Yes" if cond_result else "No")