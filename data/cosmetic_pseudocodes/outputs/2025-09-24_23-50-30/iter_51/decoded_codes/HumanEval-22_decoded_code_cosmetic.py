from typing import Any, List, Sequence


def filter_integers(collection_of_items: Sequence[Any]) -> List[int]:
    def accumulate_filtered(src: Sequence[Any], idx: int) -> List[int]:
        if idx == len(src):
            return []
        head_element = src[idx]
        filtered_rest = accumulate_filtered(src, idx + 1)
        return [head_element] + filtered_rest if isinstance(head_element, int) else filtered_rest

    return accumulate_filtered(collection_of_items, 0)