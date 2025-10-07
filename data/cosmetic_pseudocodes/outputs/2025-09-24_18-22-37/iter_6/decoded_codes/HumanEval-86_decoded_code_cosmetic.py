from typing import List


def anti_shuffle(original_text: str) -> str:
    words_collection: List[str] = original_text.split(" ")
    reordered_words: List[str] = []

    current_index: int = 0
    while current_index < len(words_collection):
        single_word: str = words_collection[current_index]

        letters_array: List[str] = list(single_word)

        temp_index1: int = 1
        while temp_index1 < len(letters_array):
            temp_index2: int = 0
            while temp_index2 < len(letters_array) - temp_index1:
                if letters_array[temp_index2] > letters_array[temp_index2 + 1]:
                    temp_char: str = letters_array[temp_index2]
                    letters_array[temp_index2] = letters_array[temp_index2 + 1]
                    letters_array[temp_index2 + 1] = temp_char
                temp_index2 += 1
            temp_index1 += 1

        reconstructed_word: str = ""
        letter_counter: int = 0
        while letter_counter < len(letters_array):
            reconstructed_word += letters_array[letter_counter]
            letter_counter += 1

        reordered_words.append(reconstructed_word)
        current_index += 1

    final_output: str = ""
    join_index: int = 0
    while join_index < len(reordered_words):
        final_output += reordered_words[join_index]
        if join_index < len(reordered_words) - 1:
            final_output += " "
        join_index += 1

    return final_output