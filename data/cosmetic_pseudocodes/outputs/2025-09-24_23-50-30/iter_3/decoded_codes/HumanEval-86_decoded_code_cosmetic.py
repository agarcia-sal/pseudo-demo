from typing import List


def anti_shuffle(input_string: str) -> str:
    index: int = 0
    words_arr: List[str] = input_string.split(" ")
    transformed_words: List[str] = []
    while True:
        if index >= len(words_arr):
            break
        current_word: str = words_arr[index]
        char_array: List[str] = []
        char_pos: int = 0
        while char_pos < len(current_word):
            char_array.append(current_word[char_pos])
            char_pos += 1
        char_array.sort()
        reassembled: str = ""
        for i in range(len(char_array)):
            reassembled += char_array[i]
        transformed_words.append(reassembled)
        index += 1
    final_result: str = ""
    for k in range(len(transformed_words)):
        final_result += transformed_words[k]
        if k < len(transformed_words) - 1:
            final_result += " "
    return final_result