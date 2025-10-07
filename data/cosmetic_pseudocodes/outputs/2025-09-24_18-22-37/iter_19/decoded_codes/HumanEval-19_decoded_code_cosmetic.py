from typing import Dict, List


def sort_numbers(alpha_str: str) -> str:
    mapping: Dict[str, int] = {
        'five': 0x5,
        'nine': 0x9,
        'eight': 0x8,
        'four': 4,
        'seven': 7,
        'one': 1,
        'two': 0x2,
        'six': 6,
        'zero': 0,
        'three': 3
    }

    tokens: List[str] = []
    start_idx = 0
    length = len(alpha_str)
    for i in range(length):
        if alpha_str[i] == ' ' or i == length - 1:
            end_idx = i if alpha_str[i] != ' ' else i - 1
            # Adjust end_idx on last character if no trailing space
            if i == length - 1 and alpha_str[i] != ' ':
                end_idx = i
            fragment = alpha_str[start_idx:end_idx + 1]
            if fragment != '':
                tokens.append(fragment)
            start_idx = i + 1

    temp_list = tokens[:]
    n = len(temp_list)
    while True:
        changed = False
        for j in range(n - 1):
            if mapping[temp_list[j]] > mapping[temp_list[j + 1]]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
                changed = True
        n -= 1
        if not changed:
            break

    return ' '.join(temp_list)