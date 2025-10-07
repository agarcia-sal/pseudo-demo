from typing import List


def anti_shuffle(input_string: str) -> str:
    temp_word_collection: List[str] = input_string.split(' ')
    reordered_words: List[str] = []
    iteration_index: int = 0
    while iteration_index < len(temp_word_collection):
        current_element: str = temp_word_collection[iteration_index]
        temp_char_sequence: List[str] = sorted(current_element)
        combined_sorted_word: str = ''.join(temp_char_sequence)
        reordered_words.append(combined_sorted_word)
        iteration_index += 1
    final_output: str = ' '.join(reordered_words)
    return final_output