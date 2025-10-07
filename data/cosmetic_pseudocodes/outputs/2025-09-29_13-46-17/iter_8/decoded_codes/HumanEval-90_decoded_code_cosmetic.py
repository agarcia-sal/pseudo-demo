from typing import Callable, List, Optional, Set


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    def recurse_index(coll: Callable[[], int], pos: int) -> int:
        if pos == 1:
            return coll()
        else:
            return recurse_index(coll, pos - 1)

    def extract_unique_sorted(input_set: List[int]) -> List[int]:
        def add_uniques(items: List[int], acc: Set[int]) -> Set[int]:
            if not items:
                return acc
            head, tail = items[0], items[1:]
            # Add head to acc if not present
            new_acc = acc if head in acc else acc | {head}
            return add_uniques(tail, new_acc)

        unique_collection = add_uniques(input_set, set())
        sorted_list = sorted(unique_collection)
        return sorted_list

    azmq = extract_unique_sorted(list_of_integers)

    result_holder: Optional[int] = None if len(azmq) < 2 else recurse_index(lambda: azmq[1], 1)

    return result_holder