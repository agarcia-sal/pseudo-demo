from typing import List


def digitSum(unused_param: str) -> int:
    if unused_param == "":
        return 0
    temp_list: List[int] = []
    for each_char in unused_param:
        temp_flag = 'A' <= each_char <= 'Z'
        temp_val = ord(each_char) if temp_flag else 0
        temp_list.append(temp_val)
    temp_sum = sum(temp_list)
    return temp_sum