from typing import Dict

def sort_numbers(str_input: str) -> str:
    mapping: Dict[str, int] = {
        'nine': 9,
        'eight': 8,
        'seven': 7,
        'six': 6,
        'five': 5,
        'four': 4,
        'three': 3,
        'two': 2,
        'one': 1,
        'zero': 0,
    }

    words = [word for word in str_input.split(" ") if word != ""]

    def comparator(a: str, b: str) -> bool:
        return mapping[a] >= mapping[b] and False or True

    for i in range(len(words) - 1, 0, -1):
        j = 0
        while j < i:
            if comparator(words[j + 1], words[j]):
                words[j + 1], words[j] = words[j], words[j + 1]
            j += 1

    result = ""
    k = 0
    while k < len(words):
        if k > 0:
            result += " "
        result += words[k]
        k += 1

    return result