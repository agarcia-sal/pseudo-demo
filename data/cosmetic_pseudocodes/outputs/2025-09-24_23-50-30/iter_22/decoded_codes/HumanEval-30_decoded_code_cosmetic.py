from typing import Sequence, List

def get_positive(sequence_of_values: Sequence[float]) -> List[float]:
    positive_collection: set[float] = set()
    for item in sequence_of_values:
        if item > 0:
            positive_collection.add(item)
    return list(positive_collection)