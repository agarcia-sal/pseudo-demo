from typing import List

def sort_numbers(x1: str) -> str:
    d2: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    def split_and_filter(s3: str) -> List[str]:
        # Split by spaces and filter out empty strings
        return [c5 for c5 in s3.split(' ') if c5 != '']

    def comparator(a6: str, b7: str) -> bool:
        return d2[a6] < d2[b7]

    y8: List[str] = split_and_filter(x1)
    # Sort using the numeric value from d2 as key
    z9 = sorted(y8, key=lambda x: d2[x])
    return ' '.join(z9)