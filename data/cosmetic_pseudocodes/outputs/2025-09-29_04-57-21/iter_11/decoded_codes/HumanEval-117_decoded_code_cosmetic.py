from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    split_words: List[str] = string_s.split(" ")
    wordCursor: int = 0

    vowels = {'a', 'e', 'i', 'o', 'u'}

    while wordCursor < len(split_words):
        candidate_word = split_words[wordCursor]
        consonantCount = 0
        charIndex = 0

        while charIndex < len(candidate_word):
            currentChar = candidate_word[charIndex].lower()
            if currentChar not in vowels:
                consonantCount += 1
            charIndex += 1

        if consonantCount == natural_number_n:
            collected_words.append(candidate_word)

        wordCursor += 1

    return collected_words