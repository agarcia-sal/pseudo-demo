from typing import List

def filter_by_prefix(sequence_of_texts: List[str], initial_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    pointer: int = 0
    while pointer < len(sequence_of_texts):
        if sequence_of_texts[pointer][:len(initial_substring)] == initial_substring:
            filtered_collection.append(sequence_of_texts[pointer])
        pointer += 1
    return filtered_collection