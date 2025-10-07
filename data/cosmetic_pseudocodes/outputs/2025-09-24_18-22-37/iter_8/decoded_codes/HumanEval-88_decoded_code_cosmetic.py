from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)  # assuming container contains integers as "+" and "%" implies numeric type

def sort_array(container: Sequence[T]) -> List[T]:
    size_metric: int = len(container)
    if size_metric != 0:
        front_element: T = container[0]
        last_element_index: int = size_metric - 1
        rear_element: T = container[last_element_index]
        combined_sum: int = front_element + rear_element
        is_desc_order_flag: bool = False
        if combined_sum % 2 == 0:
            is_desc_order_flag = True
        result_array: List[T] = sorted(container, reverse=is_desc_order_flag)
        return result_array
    else:
        return []