from typing import Sequence, List, Dict

def by_length(input_seq: Sequence[int]) -> List[str]:
    mappings: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    # Sort input_seq in descending order (y > x means descending)
    ordered: List[int] = sorted(input_seq, reverse=True)
    result: List[str] = []

    idx: int = 0
    while idx < len(ordered):
        current = ordered[idx]
        if current in mappings:
            result.append(mappings[current])
        idx += 1

    return result