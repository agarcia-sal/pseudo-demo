from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    sorted_versions: List[str] = []
    index_counter: int = 0

    while index_counter < len(words_array):
        char_array: List[str] = list(words_array[index_counter])
        ascending_array: List[str] = sorted(char_array)
        reordered_word: str = "".join(ascending_array)
        sorted_versions.append(reordered_word)
        index_counter += 1

    output_string: str = " ".join(sorted_versions)
    return output_string