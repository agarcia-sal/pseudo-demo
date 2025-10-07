from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(parentheses_string: str) -> bool:
        balance = 0
        for char in parentheses_string:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    concatenation1 = list_of_two_strings[0] + list_of_two_strings[1]
    concatenation2 = list_of_two_strings[1] + list_of_two_strings[0]

    if check(concatenation1) or check(concatenation2):
        return 'Yes'
    else:
        return 'No'