from typing import List

def sort_numbers(input_tokens: str) -> str:
    lookup: dict[str, int] = {
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
    filtered_tokens: List[str] = [token for token in input_tokens.split(' ') if token != '']
    index: int = 0
    n: int = len(filtered_tokens)
    while index < n - 1:
        swap_happened: bool = False
        for j in range(n - 1 - index):
            if lookup[filtered_tokens[j]] > lookup[filtered_tokens[j + 1]]:
                filtered_tokens[j], filtered_tokens[j + 1] = filtered_tokens[j + 1], filtered_tokens[j]
                swap_happened = True
        if not swap_happened:
            break
        index += 1
    result_string: str = ''
    for k in range(n):
        if k == 0:
            result_string = filtered_tokens[k]
        else:
            result_string += f' {filtered_tokens[k]}'
    return result_string