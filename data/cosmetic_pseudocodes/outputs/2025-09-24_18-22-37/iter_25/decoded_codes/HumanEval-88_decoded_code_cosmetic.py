from typing import List


def sort_array(parameter_list: List[int]) -> List[int]:
    if len(parameter_list) != 0:
        temp_sum: int = parameter_list[0]
        temp_end_value: int = parameter_list[len(parameter_list) - 1]
        temp_sum += temp_end_value

        sorting_direction_flag: bool = (temp_sum % 2 == 0)

        output_array: List[int] = parameter_list.copy()

        changed: bool = True
        while changed:
            changed = False
            index: int = 1
            while index < len(output_array):
                if sorting_direction_flag:
                    if output_array[index - 1] < output_array[index]:
                        temp_value: int = output_array[index]
                        output_array[index] = output_array[index - 1]
                        output_array[index - 1] = temp_value
                        changed = True
                else:
                    if output_array[index - 1] > output_array[index]:
                        temp_value = output_array[index]
                        output_array[index] = output_array[index - 1]
                        output_array[index - 1] = temp_value
                        changed = True
                index += 1

        return output_array
    else:
        return []