from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_x: str) -> bool:
        def recur(index_y: int, balance_z: int) -> bool:
            if index_y >= len(string_x):
                return balance_z == 0
            if string_x[index_y] == '(':
                new_balance_w = balance_z + 1
            else:
                new_balance_w = balance_z - 1
            if new_balance_w < 0:
                return False
            return recur(index_y + 1, new_balance_w)
        return recur(0, 0)

    first_second_v = list_of_two_strings[0] + list_of_two_strings[1]
    second_first_u = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_second_v):
        return 'Yes'
    if check(second_first_u):
        return 'Yes'
    return 'No'