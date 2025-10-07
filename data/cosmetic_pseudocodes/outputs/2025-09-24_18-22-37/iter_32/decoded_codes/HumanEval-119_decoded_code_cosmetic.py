from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter: int = 0
        idx: int = 0
        length: int = len(string_to_verify)
        while idx < length:
            ch: str = string_to_verify[idx]
            if ch == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
            idx += 1
        return counter == 0

    combined_a: str = list_of_two_strings[0] + list_of_two_strings[1]
    combined_b: str = list_of_two_strings[1] + list_of_two_strings[0]

    if not check(combined_a):
        if not check(combined_b):
            return 'No'
        else:
            return 'Yes'
    else:
        return 'Yes'