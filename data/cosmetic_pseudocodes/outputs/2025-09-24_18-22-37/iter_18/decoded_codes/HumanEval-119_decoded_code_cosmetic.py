from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        tolerance_counter = 0
        position_index = 0
        while True:
            if position_index >= len(string_to_verify):
                break
            inspected_char = string_to_verify[position_index]
            if inspected_char == '(':
                tolerance_counter += 1
            else:
                tolerance_counter -= 1
            if tolerance_counter < 0:
                return False
            position_index += 1
        return tolerance_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]
    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'