from typing import Sequence, List

def rescale_to_unit(numbers_collection: Sequence[float]) -> List[float]:
    if not numbers_collection:
        raise ValueError("numbers_collection must not be empty")

    smallest_value = numbers_collection[0]
    for index in range(1, len(numbers_collection)):
        if numbers_collection[index] < smallest_value:
            smallest_value = numbers_collection[index]

    largest_value = numbers_collection[0]
    for index in range(1, len(numbers_collection)):
        if largest_value < numbers_collection[index]:
            largest_value = numbers_collection[index]

    spread = largest_value - smallest_value
    if spread == 0:
        # Avoid division by zero if all values are the same; map all to 0.0
        return [0.0 for _ in numbers_collection]

    normalized_values = [(each_val - smallest_value) * (1 / spread) for each_val in numbers_collection]

    return normalized_values