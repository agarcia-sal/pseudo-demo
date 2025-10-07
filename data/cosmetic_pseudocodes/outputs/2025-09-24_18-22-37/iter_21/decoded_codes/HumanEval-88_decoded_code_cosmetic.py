from typing import List

def sort_array(items: List[int]) -> List[int]:
    if len(items) == 0:
        return []
    first_elem_sum: int = items[0] + items[-1]
    order_descending: bool = (first_elem_sum % 2 == 0)
    return sorted(items, reverse=order_descending)