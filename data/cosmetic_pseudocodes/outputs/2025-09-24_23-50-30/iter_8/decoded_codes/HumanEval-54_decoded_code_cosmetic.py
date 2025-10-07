from typing import Dict


def same_chars(string_zero: str, string_one: str) -> bool:
    temp_one: Dict[str, int] = {}
    temp_two: Dict[str, int] = {}

    for each_char in string_zero:
        temp_one[each_char] = 1
    for each_element in string_one:
        temp_two[each_element] = 1

    list_one = list(temp_one.keys())
    list_two = list(temp_two.keys())

    for index_i in range(len(list_one)):
        if list_one[index_i] not in list_two:
            return False
    for index_j in range(len(list_two)):
        if list_two[index_j] not in list_one:
            return False

    return True