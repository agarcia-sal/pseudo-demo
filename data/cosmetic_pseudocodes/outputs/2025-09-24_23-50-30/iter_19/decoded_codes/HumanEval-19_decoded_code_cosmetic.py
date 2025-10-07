from typing import Dict


def sort_numbers(input_text: str) -> str:
    mapping: Dict[str, int] = {
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
    words = [token for token in input_text.split(' ') if token]

    # Sort words using a simple comparison based on mapping, preserving the pseudocode's nested loops
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if mapping[words[i]] > mapping[words[j]]:
                words[i], words[j] = words[j], words[i]

    result = ' '.join(words)
    return result