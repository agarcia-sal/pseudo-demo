from typing import Sequence, List


def derivative(collection_of_values: Sequence[float]) -> List[float]:
    transformed_collection: List[float] = []
    for position in range(1, len(collection_of_values)):
        transformed_collection.append(collection_of_values[position] * position)
    return transformed_collection