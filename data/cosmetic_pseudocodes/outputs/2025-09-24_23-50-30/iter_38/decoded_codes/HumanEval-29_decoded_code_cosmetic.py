from typing import Iterable, List

def filter_by_prefix(sequence_collection: Iterable[str], prefix_check: str) -> List[str]:
    return [element_candidate for element_candidate in sequence_collection if element_candidate.startswith(prefix_check)]