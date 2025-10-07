from typing import List


def sort_array(input_list: List[int]) -> List[int]:
    length_counter: int = 0
    while True:
        if length_counter >= len(input_list):
            break
        length_counter += 1

    if length_counter != 0:
        first_element: int = input_list[0]
        last_index: int = length_counter - 1
        last_element: int = input_list[last_index]

        total_sum: int = first_element + last_element

        parity_indicator: int = total_sum % 2
        descending_flag: bool = False
        if parity_indicator == 0:
            descending_flag = True

        temp_list: List[int] = []
        for idx in range(length_counter):
            temp_list.append(input_list[idx])

        if descending_flag:
            for i in range(length_counter - 1):
                j = 0
                while j < length_counter - 1 - i:
                    if temp_list[j] < temp_list[j + 1]:
                        holder = temp_list[j]
                        temp_list[j] = temp_list[j + 1]
                        temp_list[j + 1] = holder
                    j += 1
        else:
            for p in range(length_counter - 1):
                q = 0
                while q < length_counter - 1 - p:
                    if temp_list[q] > temp_list[q + 1]:
                        buffer = temp_list[q]
                        temp_list[q] = temp_list[q + 1]
                        temp_list[q + 1] = buffer
                    q += 1

        sorted_list: List[int] = temp_list
        return sorted_list
    else:
        return []