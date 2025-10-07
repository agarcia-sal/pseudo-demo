from typing import List


def anti_shuffle(input_string: str) -> str:
    bucket_of_terms: List[str] = []
    intermediate_word_collection: List[str] = input_string.split(" ")
    index_counter: int = 0
    while index_counter < len(intermediate_word_collection):
        internal_word: str = intermediate_word_collection[index_counter]
        letter_sequence: List[str] = []
        sub_index: int = 0
        while sub_index < len(internal_word):
            letter_sequence.append(internal_word[sub_index])
            sub_index += 1
        letter_sequence.sort()
        temp_string: str = ""
        position: int = 0
        while position < len(letter_sequence):
            temp_string += letter_sequence[position]
            position += 1
        bucket_of_terms.append(temp_string)
        index_counter += 1
    assembled_result: str = ""
    element_index: int = 0
    while element_index < len(bucket_of_terms):
        assembled_result += bucket_of_terms[element_index]
        if element_index < len(bucket_of_terms) - 1:
            assembled_result += " "
        element_index += 1
    return assembled_result