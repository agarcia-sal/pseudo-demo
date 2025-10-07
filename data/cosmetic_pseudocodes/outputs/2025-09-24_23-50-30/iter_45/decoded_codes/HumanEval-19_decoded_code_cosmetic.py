from typing import Dict


def sort_numbers(string_of_number_words: str) -> str:
    mapper: Dict[str, int] = {
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
    tokens = [segment for segment in string_of_number_words.split(" ") if segment != ""]
    finally_sorted = tokens[:]

    n = len(tokens)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if mapper[finally_sorted[i]] > mapper[finally_sorted[j]]:
                finally_sorted[i], finally_sorted[j] = finally_sorted[j], finally_sorted[i]

    return " ".join(finally_sorted)