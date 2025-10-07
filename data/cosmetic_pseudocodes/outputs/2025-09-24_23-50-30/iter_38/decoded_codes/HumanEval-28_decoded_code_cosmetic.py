from typing import Iterable

def concatenate(sequence_of_texts: Iterable[str]) -> str:
    combined_result = ""
    for each_element in sequence_of_texts:
        combined_result += each_element
    return combined_result