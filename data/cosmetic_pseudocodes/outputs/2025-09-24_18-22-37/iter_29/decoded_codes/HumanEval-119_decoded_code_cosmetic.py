from typing import List

def match_parens(array_of_strings: List[str]) -> str:
    def check(text_to_test: str) -> bool:
        counter_var = 0
        for current_char in text_to_test:
            if current_char == '(':
                counter_var += 1
            else:
                counter_var -= 1
            if counter_var < 0:
                return False
        return counter_var == 0

    combo_a = array_of_strings[0] + array_of_strings[1]
    combo_b = array_of_strings[1] + array_of_strings[0]
    first_check = check(combo_a)
    second_check = check(combo_b)

    if first_check:
        return 'Yes'
    if second_check:
        return 'Yes'
    return 'No'