from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_array: List[int] = []
    toggle_switch: int = 1

    arr = array_of_numbers[:]  # Work on a copy to avoid side effects
    while arr:
        if toggle_switch == 1:
            chosen_element = arr[0]
            for element in arr:
                if element < chosen_element:
                    chosen_element = element
        else:
            chosen_element = arr[0]
            for element in arr:
                if element >= chosen_element:
                    chosen_element = element

        output_array.append(chosen_element)

        # Remove only the first occurrence of chosen_element from arr
        removed_once = False
        filtered = []
        for item in arr:
            if item == chosen_element and not removed_once:
                removed_once = True
                continue
            filtered.append(item)
        arr = filtered

        toggle_switch = 1 - toggle_switch

    return output_array