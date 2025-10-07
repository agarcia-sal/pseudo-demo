from typing import List

def vowels_count(string_input: str) -> int:
    vowels_list: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count: int = 0
    for i in range(1, len(string_input) + 1):
        # i-1 for zero-based index in string_input
        if string_input[i - 1] in vowels_list:
            count += 1
    if string_input and (string_input[-1] == 'y' or string_input[-1] == 'Y'):
        count += 1
    return count