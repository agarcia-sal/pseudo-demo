from typing import List

def vowels_count(string_input: str) -> int:
    vowelsList: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def count_vowels(idx: int, total: int) -> int:
        if idx == len(string_input):
            return total
        currentChar = string_input[idx]
        added = 1 if currentChar in vowelsList else 0
        return count_vowels(idx + 1, total + added)

    total_vowels = count_vowels(1, 0)

    if string_input and (string_input[-1] == 'Y' or string_input[-1] == 'y'):
        total_vowels += 1

    return total_vowels