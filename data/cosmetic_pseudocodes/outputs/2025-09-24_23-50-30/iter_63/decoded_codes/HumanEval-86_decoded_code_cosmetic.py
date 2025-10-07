from typing import List


def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    reordered_collection: List[str] = []
    for idx in range(len(words_array)):
        chars_arr: List[str] = list(words_array[idx])
        chars_arr.sort()
        recomposed_word: str = "".join(chars_arr)
        reordered_collection.append(recomposed_word)
    output_text: str = " ".join(reordered_collection)
    return output_text