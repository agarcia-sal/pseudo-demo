from typing import List


def count_distinct_characters(alphabetic_sequence: str) -> int:
    def compute_unique_chars(sequence: str, unique_collection: List[str], index: int) -> int:
        if index >= len(sequence):
            return len(unique_collection)

        current_symbol = sequence[index].lower()
        if current_symbol not in unique_collection:
            unique_collection.append(current_symbol)

        return compute_unique_chars(sequence, unique_collection, index + 1)

    return compute_unique_chars(alphabetic_sequence, [], 0)