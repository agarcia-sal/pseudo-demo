from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> Union[int, float, None]:
    if not list_of_elements:
        return None  # Handle empty input by returning None

    # Copy elements starting from index 1 (1-based) => skip the first element at index 0
    sorted_list = list_of_elements[1:]
    sorted_list.sort()

    n = len(sorted_list)
    if n == 0:
        return None  # If after slicing no elements remain

    if n % 2 != 0:
        # Median for odd length list: middle element (indexing 0-based)
        # Original pseudocode uses: sorted_list[(n -1)/2 + 1], 1-based indexing
        # Convert pseudocode: index = (n - 1)//2 + 1, so zero-based index = that -1 = (n -1)//2
        return sorted_list[(n - 1) // 2]
    else:
        # Median for even length: average two middle elements
        mid = n // 2
        first_val = sorted_list[mid]
        second_val = sorted_list[mid + 1]
        return (first_val + second_val) / 2.0