from typing import Iterable, List

def filter_by_prefix(collection_of_texts: Iterable[str], initial_segment: str) -> List[str]:
    return [each_element for each_element in collection_of_texts if each_element.startswith(initial_segment)]