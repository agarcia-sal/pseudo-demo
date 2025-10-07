from typing import List

def filter_by_prefix(array_of_words: List[str], initial_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator: int = 0

    while iterator < len(array_of_words):
        current_word: str = array_of_words[iterator]
        check_prefix: str = initial_substring
        is_prefix: bool = True

        position: int = 0
        while position < len(check_prefix) and is_prefix:
            if position >= len(current_word) or current_word[position] != check_prefix[position]:
                is_prefix = False
            position += 1

        if is_prefix:
            filtered_collection.append(current_word)

        iterator += 1

    return filtered_collection