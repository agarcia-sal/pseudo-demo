from typing import List


def anti_shuffle(input_string: str) -> str:
    index: int = 0
    words_collection: List[str] = input_string.split(" ")
    accumulated_sorted_words: List[str] = []

    def sort_chars(chars: List[str]) -> List[str]:
        if len(chars) <= 1:
            return chars
        pivot = chars[0]
        less = [c for c in chars[1:] if c < pivot]
        greater_equal = [c for c in chars[1:] if not (c < pivot)]
        return sort_chars(less) + [pivot] + sort_chars(greater_equal)

    while index < len(words_collection):
        current_word: str = words_collection[index]
        char_list: List[str] = list(current_word)
        sorted_chars: List[str] = sort_chars(char_list)
        sorted_word: str = "".join(sorted_chars)
        accumulated_sorted_words.append(sorted_word)
        index += 1

    output_string: str = " ".join(accumulated_sorted_words)
    return output_string