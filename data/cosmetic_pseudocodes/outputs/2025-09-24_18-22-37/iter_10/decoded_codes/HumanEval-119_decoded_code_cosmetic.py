from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        delta_counter: int = 0
        index_p: int = 0
        while index_p < len(string_to_verify):
            temp_char = string_to_verify[index_p]
            if temp_char != '(':
                delta_counter -= 1
                if delta_counter < 0:
                    return False
            else:
                delta_counter += 1
            index_p += 1
        return delta_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat):
        return 'Yes'
    if check(second_concat):
        return 'Yes'
    return 'No'