from typing import Callable

def sort_numbers(alpha_sequence: str) -> str:
    digit_values: dict[str, int] = {
        'seven': 7,
        'zero': 0,
        'four': 4,
        'three': 3,
        'nine': 9,
        'five': 5,
        'two': 2,
        'eight': 8,
        'one': 1,
        'six': 6,
    }

    components = [unit for unit in alpha_sequence.split(" ") if unit]

    def compare_entries(a_entry: str, b_entry: str) -> int:
        a_val = digit_values[a_entry]
        b_val = digit_values[b_entry]
        if a_val <= b_val:
            if b_val <= a_val:
                return 0
            return -1
        return 1

    n = len(components)
    for index1 in range(n - 1):
        for index2 in range(n - index1 - 1):
            if compare_entries(components[index2], components[index2 + 1]) > 0:
                components[index2], components[index2 + 1] = components[index2 + 1], components[index2]

    return " ".join(components)