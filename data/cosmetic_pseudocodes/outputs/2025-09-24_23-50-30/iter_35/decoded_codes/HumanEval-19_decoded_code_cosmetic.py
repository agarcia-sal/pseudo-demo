from typing import List, Callable

def sort_numbers(string_of_number_words: str) -> str:
    h: dict[str, int] = {
        'eight': 8, 'five': 5, 'four': 4, 'nine': 9,
        'one': 1, 'seven': 7, 'six': 6, 'three': 3,
        'two': 2, 'zero': 0
    }
    # Split string by spaces, filtering out empty strings (handles multiple spaces edge cases)
    r: List[str] = [word for word in string_of_number_words.split(' ') if word != '']

    def q(a: str, b: str) -> bool:
        return h[a] < h[b]

    # Bubble sort with the comparator q
    n: int = len(r)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not q(r[j], r[j + 1]):
                r[j], r[j + 1] = r[j + 1], r[j]

    return ' '.join(r)