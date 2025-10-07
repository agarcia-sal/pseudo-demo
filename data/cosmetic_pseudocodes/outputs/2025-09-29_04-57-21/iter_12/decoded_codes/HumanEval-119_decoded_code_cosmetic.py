from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter_value = 0
        pos_index = 0

        while pos_index < len(string_to_verify):
            current_char = string_to_verify[pos_index]

            if current_char != '(':
                counter_value -= 1
            else:
                counter_value += 1

            if counter_value < 0:
                return False

            pos_index += 1

        return counter_value == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return 'Yes'
    elif check(second_concat):
        return 'Yes'
    else:
        return 'No'