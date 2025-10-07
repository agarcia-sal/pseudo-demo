from typing import List, Sequence

def filter_by_prefix(sequence_collection: Sequence[str], prefix_key: str) -> List[str]:
    filtered_results: List[str] = []

    def examine_element(position: int) -> None:
        if position >= len(sequence_collection):
            return
        current_item = sequence_collection[position]
        if current_item.startswith(prefix_key):
            filtered_results.append(current_item)
        examine_element(position + 1)

    examine_element(0)
    return filtered_results