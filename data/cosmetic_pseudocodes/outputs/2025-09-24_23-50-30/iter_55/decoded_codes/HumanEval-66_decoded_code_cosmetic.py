from typing import List


def digitSum(new_input: str) -> int:
    if new_input == "":
        return 0
    temp_list: List[int] = []
    for temp_char in new_input:
        if "A" <= temp_char <= "Z":
            temp_val = ord(temp_char)
        else:
            temp_val = 0
        temp_list.append(temp_val)
    total_sum: int = sum(temp_list)
    return total_sum