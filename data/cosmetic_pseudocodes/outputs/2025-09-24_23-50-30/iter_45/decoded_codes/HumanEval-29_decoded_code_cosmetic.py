from typing import List

def filter_by_prefix(collection_names: List[str], initial_segment: str) -> List[str]:
    accumulator: List[str] = []
    counter: int = 0

    while counter < len(collection_names):
        candidate: str = collection_names[counter]

        if not (not candidate.startswith(initial_segment)):
            accumulator.append(candidate)

        counter += 1

    return accumulator