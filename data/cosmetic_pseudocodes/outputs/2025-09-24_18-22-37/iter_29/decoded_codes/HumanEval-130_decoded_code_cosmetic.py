from typing import List


def tri(number_m: int) -> List[int]:
    if number_m == 0:
        return [1]
    triangle_list: List[int] = [1, 3]
    iterator_j: int = 2
    while iterator_j <= number_m:
        remainder_check = iterator_j % 2
        if remainder_check == 0:
            temp_value = (iterator_j // 2) + 1  # integer division
            triangle_list.append(temp_value)
        else:
            index1 = iterator_j - 1
            index2 = iterator_j - 2
            sum_part = triangle_list[index1] + triangle_list[index2]
            added_part = (iterator_j + 3) // 2  # integer division
            combined_value = sum_part + added_part
            triangle_list.append(combined_value)
        iterator_j += 1
    return triangle_list