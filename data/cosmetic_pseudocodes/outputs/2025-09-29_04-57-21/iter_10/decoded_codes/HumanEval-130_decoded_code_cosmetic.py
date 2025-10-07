from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    result_list = [1, 3]
    current_index = 2
    while current_index <= integer_n:
        if current_index % 2 != 0:
            sum_value = result_list[current_index - 1] + result_list[current_index - 2] + ((current_index + 3) // 2)
            result_list.append(sum_value)
        else:
            result_list.append((current_index // 2) + 1)
        current_index += 1
    return result_list