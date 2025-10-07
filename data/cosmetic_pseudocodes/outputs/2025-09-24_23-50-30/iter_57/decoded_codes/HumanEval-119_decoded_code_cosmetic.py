from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        state_counter = 0
        for sym in string_to_verify:
            state_counter = state_counter + 1 if sym == '(' else state_counter - 1
            if state_counter < 0:
                return False
        return state_counter == 0

    str_a, str_b = list_of_two_strings
    concat_a_b = str_a + str_b
    concat_b_a = str_b + str_a

    if check(concat_a_b) or check(concat_b_a):
        return 'Yes'
    return 'No'