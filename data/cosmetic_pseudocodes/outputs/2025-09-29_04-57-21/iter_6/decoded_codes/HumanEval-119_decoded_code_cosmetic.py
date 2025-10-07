from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        depth_counter = 0
        for symbol in string_to_verify:
            if symbol == '(':
                depth_counter += 1
            else:
                depth_counter -= 1
            if depth_counter < 0:
                return False
        return depth_counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    return 'No'