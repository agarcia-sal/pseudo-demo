from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_input: str) -> bool:
        count = 0
        for character in string_input:
            count += 1 if character == '(' else -1
            if count < 0:
                return False
        return count == 0

    combination1 = list_of_two_strings[0] + list_of_two_strings[1]
    combination2 = list_of_two_strings[1] + list_of_two_strings[0]

    if check(combination1) or check(combination2):
        return "Yes"
    return "No"