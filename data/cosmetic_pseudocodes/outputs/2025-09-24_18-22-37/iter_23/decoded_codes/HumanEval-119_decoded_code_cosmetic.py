from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter = 0
        position = 0
        length = len(string_to_verify)
        while position < length:
            current_char = string_to_verify[position]
            if current_char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
            position += 1
        return counter == 0

    first_string = list_of_two_strings[0]
    second_string = list_of_two_strings[1]

    concat_a = first_string + second_string
    concat_b = second_string + first_string

    if check(concat_a):
        return 'Yes'
    if check(concat_b):
        return 'Yes'
    return 'No'