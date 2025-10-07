from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        bal = 0
        for ch in string_to_verify:
            bal += 1 if ch == '(' else -1
            if bal < 0:
                return False
        return bal == 0

    first_concat = []
    second_concat = []
    for i in range(len(list_of_two_strings[0])):
        first_concat.append(list_of_two_strings[0][i])
        second_concat.append(list_of_two_strings[1][i])

    for i in range(len(list_of_two_strings[1])):
        first_concat.append(list_of_two_strings[1][i])
        second_concat.append(list_of_two_strings[0][i])

    first_str = ''.join(first_concat)
    second_str = ''.join(second_concat)

    if check(first_str):
        return "Yes"
    if check(second_str):
        return "Yes"
    return "No"