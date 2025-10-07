from typing import List

def filter_by_prefix(array_of_texts: List[str], start_seq: str) -> List[str]:
    results_collection: List[str] = []
    index_counter: int = 0

    while index_counter < len(array_of_texts):
        current_text: str = array_of_texts[index_counter]
        if current_text.startswith(start_seq):
            results_collection.append(current_text)
        index_counter += 1

    return results_collection