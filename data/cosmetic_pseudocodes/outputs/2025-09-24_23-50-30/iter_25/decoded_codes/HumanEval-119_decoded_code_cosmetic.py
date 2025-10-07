from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        count = 0
        for current_char in string_to_verify:
            if current_char == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    concat_a = list_of_two_strings[0] + list_of_two_strings[1]
    concat_b = list_of_two_strings[1] + list_of_two_strings[0]

    if check(concat_a) or check(concat_b):
        return 'Yes'
    else:
        return 'No'