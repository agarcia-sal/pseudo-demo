from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        position_counter = 0
        index_pointer = 0
        length = len(string_to_verify)
        while index_pointer < length:
            current_symbol = string_to_verify[index_pointer]
            # Increment position_counter by 1 if '(', else decrement by 1
            position_counter += 1 if current_symbol == '(' else -1
            if position_counter < 0:
                return False
            index_pointer += 1
        return position_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return "Yes"
    if check(second_concat):
        return "Yes"
    return "No"