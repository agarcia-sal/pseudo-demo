from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter = 0
        for character in string_to_verify:
            if character == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]
    if check(first_concat) or check(second_concat):
        return "Yes"
    else:
        return "No"