from typing import List


def sort_numbers(string_of_number_words: str) -> str:
    lookup: List[tuple[str, int]] = [
        ("zero", 0), ("one", 1), ("two", 2), ("three", 3), ("four", 4),
        ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)
    ]

    tmp_words: List[str] = [token for token in string_of_number_words.split(' ') if token != ""]

    def get_value(word: str) -> int:
        for w, v in lookup:
            if w == word:
                return v
        return -1

    n: int = len(tmp_words)
    i: int = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if get_value(tmp_words[i]) > get_value(tmp_words[j]):
                tmp_words[i], tmp_words[j] = tmp_words[j], tmp_words[i]
            j += 1
        i += 1

    result = ' '.join(tmp_words)
    return result