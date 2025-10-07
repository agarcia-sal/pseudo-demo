from typing import List

def filter_by_substring(collection_of_items: List[str], sequence_pattern: str) -> List[str]:
    def loop_through(items: List[str], pattern: str, accumulator: List[str]) -> List[str]:
        if not items:
            return accumulator
        head_element, tail_elements = items[0], items[1:]
        new_accumulator = accumulator + [head_element] if pattern in head_element else accumulator
        return loop_through(tail_elements, pattern, new_accumulator)
    return loop_through(collection_of_items, sequence_pattern, [])