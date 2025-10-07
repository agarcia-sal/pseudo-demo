from typing import Optional, Sequence

def longest(sequence_strings: Sequence[str]) -> Optional[str]:
    if not sequence_strings:
        return None

    len_records = [len(x) for x in sequence_strings]

    max_val: Optional[int] = None
    for num in len_records:
        if max_val is None or num > max_val:
            max_val = num

    idx = 0
    while idx < len(sequence_strings):
        if len(sequence_strings[idx]) == max_val:
            return sequence_strings[idx]
        idx += 1

    return None  # In case no string found, though logically unreachable