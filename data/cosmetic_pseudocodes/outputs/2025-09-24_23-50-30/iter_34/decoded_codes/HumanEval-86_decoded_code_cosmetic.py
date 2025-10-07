from typing import Dict, List

def anti_shuffle(input_string: str) -> str:
    word_map: Dict[int, str] = {}
    word_sequence: List[str] = input_string.split(" ")
    length = len(word_sequence)

    def process_words(idx: int) -> None:
        if idx == length:
            return
        current_word = word_sequence[idx]
        char_array = list(current_word)
        char_array.sort()  # sort ascending

        reordered_word = ""
        pos = 0
        while pos < len(char_array):
            reordered_word += char_array[pos]
            pos += 1

        word_map[idx] = reordered_word
        process_words(idx + 1)

    process_words(0)

    result_parts: List[str] = []
    key = 0
    while key < len(word_map):
        result_parts.append(word_map[key])
        key += 1

    final_string = ""
    counter = 0
    while counter < len(result_parts):
        final_string += result_parts[counter]
        if counter < len(result_parts) - 1:
            final_string += " "
        counter += 1

    return final_string