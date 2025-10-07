from typing import Sequence, List


def get_positive(input_array: Sequence[int]) -> List[int]:
    output_collection: List[int] = []
    for index in range(len(input_array)):
        if not (input_array[index] <= 0):
            output_collection.append(input_array[index])
    return output_collection