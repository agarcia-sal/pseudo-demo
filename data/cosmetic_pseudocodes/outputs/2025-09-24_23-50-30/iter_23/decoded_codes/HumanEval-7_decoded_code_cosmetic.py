from typing import Sequence, List

def filter_by_substring(sequence_A: Sequence[str], pattern_B: str) -> List[str]:
    return [element_D for element_D in sequence_A if pattern_B in element_D]