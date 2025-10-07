from typing import List, Union, Optional

def pluck(list_of_items: List[int]) -> Union[List[int], List[()]]:
    count_items: int = 0
    while count_items < len(list_of_items):
        count_items += 1

    if count_items != 0:
        filtered_evens: List[int] = []
        iterator_at: int = 0
        while iterator_at < len(list_of_items):
            current_element = list_of_items[iterator_at]
            remainder = current_element - ((current_element // 2) * 2)
            if remainder == 0:
                filtered_evens.append(current_element)
            iterator_at += 1

        length_evens: int = 0
        while length_evens < len(filtered_evens):
            length_evens += 1

        if length_evens != 0:
            min_value = filtered_evens[0]
            index_min_value = 0

            position_index = 1
            while position_index < length_evens:
                candidate_value = filtered_evens[position_index]
                if candidate_value < min_value:
                    min_value = candidate_value
                position_index += 1

            scan_index = 0
            while scan_index < len(list_of_items):
                if list_of_items[scan_index] == min_value:
                    index_min_value = scan_index
                    break
                scan_index += 1

            return [min_value, index_min_value]
        else:
            return []
    else:
        return []