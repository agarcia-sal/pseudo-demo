from collections import Counter
from typing import List

def strange_sort_list(original_collection: List[int]) -> List[int]:
    def helper(accumulated: List[int], remaining_collection: List[int], switch: bool) -> List[int]:
        if not remaining_collection:
            return accumulated

        candidates = remaining_collection
        chosen_element = min(candidates) if switch else max(candidates)
        updated_accumulated = accumulated + [chosen_element]

        # Count elements to remove only one occurrence of chosen_element
        remaining_counts = Counter(remaining_collection)
        remaining_counts[chosen_element] -= 1

        # Rebuild list from count, excluding elements with count zero
        updated_remaining = [x for x, cnt in remaining_counts.items() for _ in range(cnt) if cnt > 0]

        return helper(updated_accumulated, updated_remaining, not switch)

    return helper([], original_collection, True)