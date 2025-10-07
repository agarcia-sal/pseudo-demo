from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_input: str) -> bool:
        counter = 0
        i = 0
        while i < len(string_input):
            ch = string_input[i]
            if ch == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
            i += 1
        return counter == 0

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    else:
        return 'No'