from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}

    def count_consonants(w: str) -> int:
        if len(w) == 0:
            return 0
        first_char = w[0].lower()
        tail_count = count_consonants(w[1:])
        return tail_count if first_char in vowels else tail_count + 1

    words = string_s.split()
    output: List[str] = []
    for word_index in range(len(words) - 1, -1, -1):
        word = words[word_index]
        if count_consonants(word) != natural_number_n:
            continue
        output.append(word)

    return output