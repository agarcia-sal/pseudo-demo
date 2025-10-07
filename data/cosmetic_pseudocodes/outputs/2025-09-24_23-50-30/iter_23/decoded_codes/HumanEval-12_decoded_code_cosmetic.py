from typing import Sequence, Optional

def longest(sequence_of_words: Sequence[str]) -> Optional[str]:
    if not sequence_of_words:
        return None

    peak_size: int = 0
    for item in sequence_of_words:
        current_size = len(item)
        if current_size > peak_size:
            peak_size = current_size

    for entity in sequence_of_words:
        if len(entity) == peak_size:
            return entity

    return None  # fallback, though logically unreachable