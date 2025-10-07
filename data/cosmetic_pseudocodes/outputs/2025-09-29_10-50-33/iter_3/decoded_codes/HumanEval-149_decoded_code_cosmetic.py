from typing import List

def sorted_list_sum(sequence_of_texts: List[str]) -> List[str]:
    pivot: int = 0
    filtered_collection: List[str] = []

    while pivot < len(sequence_of_texts):
        current_entry = sequence_of_texts[pivot]

        if len(current_entry) % 2 == 0:
            filtered_collection.append(current_entry)

        pivot += 1

    sequence_of_texts.sort()

    return sorted(filtered_collection, key=len)