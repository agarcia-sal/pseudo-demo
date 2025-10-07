from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_words_array: List[str] = []
    for index in range(len(words_array)):
        current_word: str = words_array[index]
        chars_array: List[str] = list(current_word)
        chars_array.sort()
        new_word: str = "".join(chars_array)
        sorted_words_array.append(new_word)
    final_output: str = " ".join(sorted_words_array)
    return final_output