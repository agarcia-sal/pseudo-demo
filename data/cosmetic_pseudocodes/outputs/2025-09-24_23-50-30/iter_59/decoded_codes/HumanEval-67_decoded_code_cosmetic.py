from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def helper_function(list_param: List[str], index_param: int, acc_param: int) -> int:
        if index_param >= len(list_param):
            return acc_param
        if not list_param[index_param].isdigit():
            return helper_function(list_param, index_param + 1, acc_param)
        return helper_function(list_param, index_param + 1, acc_param + int(list_param[index_param]))

    temp_0: List[str] = string_description.split(" ")
    temp_1: int = helper_function(temp_0, 0, 0)
    temp_2: int = total_number_of_fruits - temp_1
    return temp_2