from typing import List


def match_parens(arr_of_two_strings: List[str]) -> str:
    def check(str_verify: str) -> bool:
        count_balance = 0
        for ch in str_verify:
            if ch == '(':
                count_balance += 1
            else:
                count_balance -= 1
            if count_balance < 0:
                return False
        return count_balance == 0

    concat_a = arr_of_two_strings[0] + arr_of_two_strings[1]
    concat_b = arr_of_two_strings[1] + arr_of_two_strings[0]

    return "Yes" if check(concat_a) or check(concat_b) else "No"