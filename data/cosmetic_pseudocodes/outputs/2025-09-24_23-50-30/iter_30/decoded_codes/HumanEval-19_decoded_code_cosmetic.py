from typing import List, Dict


def sort_numbers(bin_string: str) -> str:
    val_table: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    parts: List[str] = [c for c in bin_string.split(' ') if c]

    def qsort(xs: List[str]) -> List[str]:
        if not xs:
            return []
        p = xs[0]
        left_side = [x for x in xs[1:] if val_table[x] <= val_table[p]]
        right_side = [x for x in xs[1:] if val_table[x] > val_table[p]]
        return qsort(left_side) + [p] + qsort(right_side)

    ordered = qsort(parts)
    return ' '.join(ordered)