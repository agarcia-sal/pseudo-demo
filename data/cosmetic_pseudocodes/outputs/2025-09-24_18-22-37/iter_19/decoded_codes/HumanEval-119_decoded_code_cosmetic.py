from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counting_balance: int = 0
        cursor_index: int = 0

        while cursor_index < len(string_to_verify):
            current_char: str = string_to_verify[cursor_index]
            if current_char != '(':
                counting_balance -= 1
            else:
                counting_balance += 1
            if counting_balance < 0:
                return False
            cursor_index += 1

        return counting_balance == 0

    first_concat: str = ""
    second_concat: str = ""
    index_run: int = 0

    while index_run < 2:
        if index_run == 0:
            first_concat = list_of_two_strings[0] + list_of_two_strings[1]
            second_concat = list_of_two_strings[1] + list_of_two_strings[0]
        index_run += 1

    result_first: bool = check(first_concat)
    result_second: bool = check(second_concat)

    if result_first or result_second:
        return "Yes"
    else:
        return "No"