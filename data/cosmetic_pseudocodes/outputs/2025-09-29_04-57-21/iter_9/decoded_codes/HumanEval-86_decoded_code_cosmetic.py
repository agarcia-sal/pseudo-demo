from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    processed_words: List[str] = []
    idx: int = 0
    while idx < len(words_array):
        current_word: str = words_array[idx]
        chars_array: List[str] = list(current_word)
        i: int = 1
        while i < len(chars_array):
            j: int = i
            while j > 0 and ord(chars_array[j]) < ord(chars_array[j - 1]):
                chars_array[j], chars_array[j - 1] = chars_array[j - 1], chars_array[j]
                j -= 1
            i += 1
        ordered_word: str = ''.join(chars_array)
        processed_words.append(ordered_word)
        idx += 1
    final_output: str = ' '.join(processed_words)
    return final_output