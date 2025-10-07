from typing import List

def order_by_points(input_array: List[int]) -> List[int]:
    def sum_of_digits(value: int) -> int:
        sign_flag = 1
        if value < 0:
            value = -value
            sign_flag = -1
        digit_components: List[int] = []
        temp_value = value
        while temp_value > 0:
            digit_components.append(temp_value % 10)
            temp_value = (temp_value - (temp_value % 10)) // 10
        if digit_components:
            digit_components[0] *= sign_flag
        else:
            # Handle the case when value == 0
            digit_components.append(0)
        total_sum = 0
        index = 0
        while index < len(digit_components):
            total_sum += digit_components[index]
            index += 1
        return total_sum

    sorted_result: List[int] = []
    remaining_items = input_array.copy()

    while len(remaining_items) > 0:
        min_index = 0
        position = 1
        while position < len(remaining_items):
            if sum_of_digits(remaining_items[position]) < sum_of_digits(remaining_items[min_index]):
                min_index = position
            position += 1
        sorted_result.append(remaining_items[min_index])
        del remaining_items[min_index]

    return sorted_result