from typing import Iterable, List

def filter_by_substring(sequence_of_texts: Iterable[str], target_sequence: str) -> List[str]:
    # Return list of texts containing the target_sequence as a substring
    return [text_element for text_element in sequence_of_texts if target_sequence in text_element]