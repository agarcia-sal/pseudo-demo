from typing import List

def filter_by_prefix(sequence_collection: List[str], starter_sequence: str) -> List[str]:
    accumulator: List[str] = []

    def accumulate(index: int) -> List[str]:
        if index >= len(sequence_collection):
            return accumulator
        element = sequence_collection[index]
        if element.startswith(starter_sequence):
            accumulator.append(element)
        return accumulate(index + 1)

    return accumulate(0)