from typing import List


def sort_numbers(input_string: str) -> str:
    mapping: dict[str, int] = {
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
    words: List[str] = [token for token in input_string.split(" ") if token != ""]

    def compare(x: str, y: str) -> bool:
        return mapping[x] < mapping[y]

    n: int = len(words)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if not compare(words[i], words[j]):
                words[i], words[j] = words[j], words[i]

    return " ".join(words)