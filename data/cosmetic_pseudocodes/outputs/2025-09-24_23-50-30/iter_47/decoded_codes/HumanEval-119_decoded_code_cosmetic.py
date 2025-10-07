from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter_x = 0
        for symbol_y in string_to_verify:
            if symbol_y == '(':
                counter_x += 1
            else:
                counter_x -= 1
            if counter_x < 0:
                return False
        return counter_x == 0

    combined_a = list_of_two_strings[0] + list_of_two_strings[1]
    combined_b = list_of_two_strings[1] + list_of_two_strings[0]
    if check(combined_a) or check(combined_b):
        return "Yes"
    return "No"