from typing import List


def anti_shuffle(input_string: str) -> str:
    def process_words(words: List[str], index: int, sorted_words: List[str]) -> List[str]:
        if index >= len(words):
            return sorted_words
        current = words[index]
        chars = [current[i] for i in range(len(current))]  # extract chars explicitly
        chars.sort()
        sorted_w = "".join(chars)
        return process_words(words, index + 1, sorted_words + [sorted_w])

    words_list = input_string.split(" ")
    all_sorted_words = process_words(words_list, 0, [])
    final_string = ""
    for idx in range(len(all_sorted_words)):
        final_string += all_sorted_words[idx]
        if idx < len(all_sorted_words) - 1:
            final_string += " "
    return final_string