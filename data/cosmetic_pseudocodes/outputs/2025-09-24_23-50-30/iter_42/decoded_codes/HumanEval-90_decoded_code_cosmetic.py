from typing import List, Optional, Set

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    def gather_uniques(src_list: List[int], acc_set: Set[int]) -> Set[int]:
        if not src_list:
            return acc_set
        head_element = src_list[0]
        tail_list = src_list[1:]
        if head_element in acc_set:
            return gather_uniques(tail_list, acc_set)
        else:
            return gather_uniques(tail_list, acc_set | {head_element})

    collected_uniques = gather_uniques(list_of_integers, set())
    sorted_uniques = sorted(collected_uniques)

    if len(sorted_uniques) < 2:
        return None
    else:
        return sorted_uniques[1]