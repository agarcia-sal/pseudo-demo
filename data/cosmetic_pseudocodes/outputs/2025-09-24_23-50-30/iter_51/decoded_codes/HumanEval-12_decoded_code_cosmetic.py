from typing import Sequence, Optional


def longest(sequence_of_texts: Sequence[str]) -> Optional[str]:
    length_of_longest: int = 0

    def find_max_length(idx: int) -> None:
        nonlocal length_of_longest
        if idx >= len(sequence_of_texts):
            return
        current_len = len(sequence_of_texts[idx])
        if current_len > length_of_longest:
            length_of_longest = current_len
        find_max_length(idx + 1)

    if len(sequence_of_texts) == 0:
        return None

    find_max_length(0)

    def locate(pos: int) -> Optional[str]:
        if pos >= len(sequence_of_texts):
            return None
        if len(sequence_of_texts[pos]) == length_of_longest:
            return sequence_of_texts[pos]
        return locate(pos + 1)

    return locate(0)