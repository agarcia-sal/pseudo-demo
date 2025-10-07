from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    output_collection: List[int] = []
    toggle_selector: bool = False
    # Work on a copy to avoid mutating the original list
    nums = list_of_integers[:]
    while nums:
        if not toggle_selector:
            chosen_element = min(nums)  # smallest element
        else:
            chosen_element = max(nums)  # largest element
        output_collection.append(chosen_element)
        nums.remove(chosen_element)
        toggle_selector = not toggle_selector
    return output_collection