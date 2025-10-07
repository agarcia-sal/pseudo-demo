from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    reordered_collection: List[int] = []
    pick_minimum: bool = True

    def process_collection(items: List[int], toggle: bool, accumulated: List[int]) -> List[int]:
        if not items:
            return accumulated

        chosen_element = min(items) if toggle else max(items)
        items.remove(chosen_element)
        accumulated.append(chosen_element)

        return process_collection(items, not toggle, accumulated)

    return process_collection(list_of_integers, pick_minimum, reordered_collection)