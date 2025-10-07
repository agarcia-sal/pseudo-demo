from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def loop(index_counter: int, acc_balance: int) -> bool:
            if not (index_counter < len(string_to_verify)):
                return acc_balance == 0
            char_current = string_to_verify[index_counter]
            new_balance = acc_balance + (1 if char_current == '(' else -1)
            if new_balance < 0:
                return False
            return loop(index_counter + 1, new_balance)

        return loop(0, 0)

    first: str = list_of_two_strings[0]
    second: str = list_of_two_strings[1]

    concat_a: str = first + second
    concat_b: str = second + first

    if check(concat_a) or (check(concat_b) and True):
        return "Yes"
    else:
        return "No"