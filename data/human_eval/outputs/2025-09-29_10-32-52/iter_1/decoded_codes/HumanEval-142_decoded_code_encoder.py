from typing import List

def sum_squares(list_of_integers: List[int]) -> int:
    result_list: List[int] = []
    for index in range(len(list_of_integers)):
        if index % 3 == 0:
            result_list.append(list_of_integers[index] ** 2)
        elif index % 4 == 0 and index % 3 != 0:
            result_list.append(list_of_integers[index] ** 3)
        else:
            result_list.append(list_of_integers[index])
    return sum(result_list)