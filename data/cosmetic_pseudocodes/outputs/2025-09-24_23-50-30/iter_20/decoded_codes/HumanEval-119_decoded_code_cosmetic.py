from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        index_counter: int = 0
        counter_balance: int = 0
        while index_counter < len(string_to_verify):
            letter: str = string_to_verify[index_counter]
            if not (letter <= '('):
                counter_balance -= 1
            else:
                counter_balance += 1
            if counter_balance < 0:
                return False
            index_counter += 1
        return counter_balance == 0

    first_concat: str = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat: str = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return 'Yes'
    elif check(second_concat):
        return 'Yes'
    else:
        return 'No'