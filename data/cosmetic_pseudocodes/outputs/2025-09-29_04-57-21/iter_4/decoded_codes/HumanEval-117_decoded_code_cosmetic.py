from typing import List, Iterator, Optional


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    words_iterator: Iterator[str] = iter(string_s.split(' '))

    vowels = {'a', 'e', 'i', 'o', 'u'}
    while True:
        current_word: Optional[str] = next(words_iterator, None)
        if current_word is None:
            break

        consonant_count = 0
        position = 0
        length = len(current_word)
        while position < length:
            letter_lower = current_word[position].lower()
            if letter_lower not in vowels:
                consonant_count += 1
            position += 1

        if consonant_count == natural_number_n:
            collected_words.append(current_word)

    return collected_words