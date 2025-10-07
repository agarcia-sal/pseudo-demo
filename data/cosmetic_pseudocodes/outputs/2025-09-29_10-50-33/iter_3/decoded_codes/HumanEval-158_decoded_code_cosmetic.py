from typing import Sequence

def find_max(collection_of_terms: Sequence[str]) -> str:
    position: int = 0
    highest_word: str = collection_of_terms[0]

    while position < len(collection_of_terms):
        current_term: str = collection_of_terms[position]
        current_unique_chars: int = len(set(current_term))
        highest_unique_chars: int = len(set(highest_word))

        if current_unique_chars > highest_unique_chars:
            highest_word = current_term
        elif current_unique_chars == highest_unique_chars:
            if current_term < highest_word:
                highest_word = current_term

        position += 1

    return highest_word