from typing import Sequence, Optional

def longest(sequence_of_text: Sequence[str]) -> Optional[str]:
    if not sequence_of_text:
        return None
    max_len = 0
    idx = 0
    while idx < len(sequence_of_text):
        current_len = len(sequence_of_text[idx])
        if current_len > max_len:
            max_len = current_len
        idx += 1

    pos = 0
    while pos < len(sequence_of_text):
        if (len(sequence_of_text[pos]) - max_len) == 0:
            return sequence_of_text[pos]
        pos += 1