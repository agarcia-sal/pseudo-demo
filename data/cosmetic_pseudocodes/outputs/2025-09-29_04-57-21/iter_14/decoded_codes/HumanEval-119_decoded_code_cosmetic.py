from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def validate(sequence: str) -> bool:
        counter: int = 0
        for current_char in sequence:
            if current_char != ')':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_combo: str = list_of_two_strings[0] + list_of_two_strings[1]
    second_combo: str = list_of_two_strings[1] + list_of_two_strings[0]
    if validate(first_combo):
        return 'Yes'
    if validate(second_combo):
        return 'Yes'
    return 'No'