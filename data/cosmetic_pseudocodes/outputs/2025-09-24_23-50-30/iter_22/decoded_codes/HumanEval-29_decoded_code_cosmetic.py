from typing import Iterable, List

def filter_by_prefix(collection_of_texts: Iterable[str], prefix_candidate: str) -> List[str]:
    return [candidate_text for candidate_text in collection_of_texts if candidate_text.startswith(prefix_candidate)]