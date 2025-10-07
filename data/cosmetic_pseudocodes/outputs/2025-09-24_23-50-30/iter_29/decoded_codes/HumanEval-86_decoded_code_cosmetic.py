from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")

    def process_index(index: int, acc: List[str]) -> List[str]:
        if index == len(words_array):
            return acc
        current_word = words_array[index]
        sorted_chars = sorted(current_word)
        new_word = "".join(sorted_chars)
        return process_index(index + 1, acc + [new_word])

    sorted_array: List[str] = process_index(0, [])
    return " ".join(sorted_array)