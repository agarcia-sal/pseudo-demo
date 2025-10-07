from typing import Sequence, Optional

def longest(sequence_of_entries: Sequence[str]) -> Optional[str]:
    if not sequence_of_entries:
        return None

    peak_length = max(len(entry) for entry in sequence_of_entries)

    for candidate in sequence_of_entries:
        if len(candidate) == peak_length:
            return candidate
    return None  # for completeness if no candidate found, though logically unreachable