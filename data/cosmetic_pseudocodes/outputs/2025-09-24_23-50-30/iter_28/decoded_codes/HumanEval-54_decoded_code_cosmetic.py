from typing import Sequence, Set

def same_chars(input_alpha: Sequence[str], input_bravo: Sequence[str]) -> bool:
    def collect_unique_chars(sequence: Sequence[str], index: int, collected: Set[str]) -> Set[str]:
        if index >= len(sequence):
            return collected
        collected_with_current = collected | {sequence[index]}  # Add current char to set
        return collect_unique_chars(sequence, index + 1, collected_with_current)

    unique_chars_alpha = collect_unique_chars(input_alpha, 0, set())
    unique_chars_bravo = collect_unique_chars(input_bravo, 0, set())

    return unique_chars_alpha == unique_chars_bravo