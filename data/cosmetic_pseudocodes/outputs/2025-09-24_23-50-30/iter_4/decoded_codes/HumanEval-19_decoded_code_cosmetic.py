from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    lookups: List[str] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    def extract_words(index: int, words_accum: List[str]) -> List[str]:
        if index >= len(string_of_number_words):
            return words_accum
        start_pos = index
        while index < len(string_of_number_words) and string_of_number_words[index] != ' ':
            index += 1
        current_word = string_of_number_words[start_pos:index]
        # Only add non-empty words (handles consecutive spaces)
        return extract_words(index + 1, words_accum + ([current_word] if current_word else []))

    tokens: List[str] = extract_words(0, [])

    def numeric_sort(a: str, b: str) -> bool:
        # True if 'a' comes before 'b' numerically, False otherwise
        return lookups.index(a) < lookups.index(b)

    sorted_tokens: List[str] = []
    for each_word in tokens:
        sorted_tokens.append(each_word)

    n: int = len(sorted_tokens)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if not numeric_sort(sorted_tokens[i], sorted_tokens[j]):
                sorted_tokens[i], sorted_tokens[j] = sorted_tokens[j], sorted_tokens[i]

    return ' '.join(sorted_tokens)