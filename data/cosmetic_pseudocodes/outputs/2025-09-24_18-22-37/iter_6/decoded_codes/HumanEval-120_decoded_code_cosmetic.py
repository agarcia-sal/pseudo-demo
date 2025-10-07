from typing import List

def maximum(input_sequence: List[int], threshold: int) -> List[int]:
    if threshold == 0:
        return []
    input_sequence.sort()  # sorts in non-decreasing order
    length_of_sequence = len(input_sequence)
    starting_index = length_of_sequence - threshold
    result: List[int] = []
    counter = starting_index
    while counter < length_of_sequence:
        result.append(input_sequence[counter])
        counter += 1
    return result