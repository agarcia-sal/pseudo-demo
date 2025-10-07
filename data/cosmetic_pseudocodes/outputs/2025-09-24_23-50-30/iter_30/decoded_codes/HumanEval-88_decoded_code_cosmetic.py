from typing import List

def sort_array(data: List[int]) -> List[int]:
    length = len(data)
    if length == 0:
        return []
    x = data[0] + data[length - 1]
    order_flag = (x % 2 == 0)
    # If order_flag is True, sort descending, else ascending
    return sorted(data, reverse=order_flag)