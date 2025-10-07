from typing import List, Optional


def next_smallest(numbers_sequence: List[int]) -> Optional[int]:
    def extract_unique_sorted(items: List[int], acc: List[int]) -> List[int]:
        if not items:
            return acc
        current_item, *remaining_items = items
        if current_item in acc:
            return extract_unique_sorted(remaining_items, acc)
        else:
            return extract_unique_sorted(remaining_items, acc + [current_item])

    unique_items = extract_unique_sorted(numbers_sequence, [])
    sorted_unique = sorted(unique_items)
    if len(sorted_unique) <= 1:
        return None
    else:
        return sorted_unique[1]