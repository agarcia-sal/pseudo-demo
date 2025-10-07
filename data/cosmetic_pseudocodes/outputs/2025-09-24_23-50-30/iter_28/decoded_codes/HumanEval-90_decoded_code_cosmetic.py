from typing import Optional, Sequence, List


def next_smallest(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    def extract_unique_sorted(collection: Sequence[int]) -> List[int]:
        seen = set()
        container = []
        for item in collection:
            if item not in seen:
                seen.add(item)
                container.append(item)
        return sorted(container)

    processed_collection = extract_unique_sorted(sequence_of_numbers)

    if len(processed_collection) < 2:
        return None
    else:
        return processed_collection[1]