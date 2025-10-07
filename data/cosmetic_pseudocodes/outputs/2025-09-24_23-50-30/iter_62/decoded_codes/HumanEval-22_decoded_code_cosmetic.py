from typing import Iterable, List, Union

def filter_integers(collection_of_items: Iterable[object]) -> List[int]:
    def helper(sequence: Iterable[object], accumulator: List[int]) -> List[int]:
        sequence_list = list(sequence)
        if not sequence_list:
            return accumulator
        head_item, *tail_items = sequence_list
        new_acc = accumulator + [head_item] if isinstance(head_item, int) else accumulator
        return helper(tail_items, new_acc)
    return helper(collection_of_items, [])