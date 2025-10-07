from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def build_answer(
        accumulator: List[T], left_list: List[T], right_list: List[T]
    ) -> List[T]:
        if left_list and right_list:
            # Both lists non-empty: take head from each and recurse
            return build_answer(
                accumulator + [left_list[0], right_list[0]], left_list[1:], right_list[1:]
            )
        elif left_list and not right_list:
            # Right list empty, append remaining left_list
            return accumulator + left_list
        else:
            # Both lists empty
            return accumulator

    step_count = 2
    even_list: List[T] = []
    idx_even = 0
    length = len(list_of_elements)
    while idx_even * step_count < length:
        even_list.append(list_of_elements[idx_even * step_count])
        idx_even += 1

    odd_list: List[T] = []
    idx_odd = 0
    while idx_odd * step_count + 1 < length:
        odd_list.append(list_of_elements[idx_odd * step_count + 1])
        idx_odd += 1

    sorted_even_list = even_list.copy()
    sorted_even_list.sort()  # sort in non-decreasing order

    return build_answer([], sorted_even_list, odd_list)