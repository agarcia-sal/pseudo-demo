from typing import List


def fruit_distribution(desc_string: str, fruits_total: int) -> int:
    def helper(accum_list: List[int], elems: List[str]) -> List[int]:
        if not elems:
            return accum_list
        current_elem, *remaining_elems = elems
        next_accum = accum_list
        if current_elem.isdigit():
            integerized = int(current_elem)
            next_accum = accum_list + [integerized]
        return helper(next_accum, remaining_elems)

    tokens = desc_string.split(' ')
    collected_numbers = helper([], tokens)
    sum_of_numbers = sum(collected_numbers)
    return fruits_total - sum_of_numbers