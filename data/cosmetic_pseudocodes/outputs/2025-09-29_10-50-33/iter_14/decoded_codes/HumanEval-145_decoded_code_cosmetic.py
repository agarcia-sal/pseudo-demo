from typing import List

def order_by_points(collection_of_values: List[int]) -> List[int]:
    def digits_sum(value: int) -> int:
        sign_flag = 1
        if value < 0:
            value = -value
            sign_flag = -1

        components: List[int] = []
        index_counter = 0
        str_value = str(value)
        while index_counter < len(str_value):
            current_char = str_value[index_counter]
            components.append(int(current_char))
            index_counter += 1

        components[0] *= sign_flag

        accumulator = 0
        pointer = 0
        while pointer < len(components):
            accumulator += components[pointer]
            pointer += 1

        return accumulator

    sorted_list: List[int] = []
    unsorted_copy = collection_of_values[:]
    while len(unsorted_copy) > 0:
        minimal_index = 0
        iter_index = 1
        while iter_index < len(unsorted_copy):
            if digits_sum(unsorted_copy[iter_index]) < digits_sum(unsorted_copy[minimal_index]):
                minimal_index = iter_index
            iter_index += 1

        sorted_list.append(unsorted_copy[minimal_index])
        unsorted_copy = unsorted_copy[:minimal_index] + unsorted_copy[minimal_index + 1 :]

    return sorted_list