from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    transformed_words: List[str] = []
    for index in range(len(words_array)):
        chars: List[str] = list(words_array[index])
        chars.sort()
        merged_word: str = "".join(chars)
        transformed_words.append(merged_word)
    final_output: str = " ".join(transformed_words)
    return final_output