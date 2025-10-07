from typing import Dict, List

def sort_numbers(string_of_number_words: str) -> str:
    digit_values: Dict[str, int] = {
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

    filtered_words: List[str] = []
    words = string_of_number_words.split()

    def collect_words(idx: int) -> None:
        if idx >= len(words):
            return
        candidate = words[idx]
        if candidate != '':
            filtered_words.append(candidate)
        collect_words(idx + 1)

    collect_words(0)

    sorted_words = sorted(filtered_words, key=lambda word: digit_values[word])

    output_parts: List[str] = []

    def build_output(i: int) -> None:
        if i >= len(sorted_words):
            return
        if i == 0:
            output_parts.append(sorted_words[i])
        else:
            output_parts.append(' ' + sorted_words[i])
        build_output(i + 1)

    build_output(0)

    return ''.join(output_parts)