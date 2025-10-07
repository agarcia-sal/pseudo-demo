from typing import List, Optional

def next_smallest(array_of_numbers: List[int]) -> Optional[int]:
    def extract_unique_sorted(sequence: List[int], idx: int, collector: List[int]) -> List[int]:
        if idx >= len(sequence):
            return collector
        current_val = sequence[idx]
        if current_val not in collector:
            collector.append(current_val)
        return extract_unique_sorted(sequence, idx + 1, collector)

    temp_collection = extract_unique_sorted(array_of_numbers, 1, [])
    sorted_collection: List[int] = []
    while temp_collection:
        min_val = temp_collection[0]
        for val in temp_collection[1:]:
            if val < min_val:
                min_val = val
        sorted_collection.append(min_val)
        temp_collection.remove(min_val)

    if len(sorted_collection) < 2:
        return None
    return sorted_collection[1]