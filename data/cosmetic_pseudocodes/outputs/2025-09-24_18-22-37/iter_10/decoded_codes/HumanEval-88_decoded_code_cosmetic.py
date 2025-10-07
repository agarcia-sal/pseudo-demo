from typing import List

def sort_array(input_data: List[int]) -> List[int]:
    if len(input_data) != 0:
        initial_element: int = input_data[0]
        terminal_element: int = input_data[-1]
        combined_sum: int = initial_element + terminal_element
        sort_desc_flag: bool = (combined_sum % 2 == 0)

        result_list: List[int] = sorted(input_data, reverse=sort_desc_flag)
        return result_list
    else:
        return []