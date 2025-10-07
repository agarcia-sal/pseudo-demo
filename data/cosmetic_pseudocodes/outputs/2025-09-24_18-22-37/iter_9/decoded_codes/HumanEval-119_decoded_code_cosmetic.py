from typing import List


def match_parens(array_of_strings: List[str]) -> str:
    def check(text_to_analyze: str) -> bool:
        count_balance: int = 0
        for current_char in text_to_analyze:
            if current_char == '(':
                count_balance += 1
            else:
                count_balance -= 1
            if count_balance < 0:
                return False
        return count_balance == 0

    first_concat: str = array_of_strings[0] + array_of_strings[1]
    second_concat: str = array_of_strings[1] + array_of_strings[0]
    condition_one: bool = check(first_concat)
    condition_two: bool = check(second_concat)

    return "Yes" if condition_one or condition_two else "No"