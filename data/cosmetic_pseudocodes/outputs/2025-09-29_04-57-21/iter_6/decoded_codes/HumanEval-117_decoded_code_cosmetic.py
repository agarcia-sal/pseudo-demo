from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    segments = string_s.split(" ")
    for segment in segments:
        consonant_count = 0
        pos = 0
        while pos < len(segment):
            current_char = segment[pos].lower()
            if current_char not in vowels:
                consonant_count += 1
            pos += 1
        if consonant_count == natural_number_n:
            collected_words.append(segment)
    return collected_words