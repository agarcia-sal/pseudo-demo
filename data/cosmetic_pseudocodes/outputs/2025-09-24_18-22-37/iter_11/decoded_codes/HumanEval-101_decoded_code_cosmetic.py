from typing import List

def words_string(parameter_string: str) -> List[str]:
    auxiliary_characters: List[str] = []
    pointer_index: int = 0
    element_char: str | None = None
    reconstructed_string: str = ""
    result_words: List[str] = []

    if parameter_string == "":
        result_words = []
    else:
        pointer_index = 0
        while pointer_index < len(parameter_string):
            element_char = parameter_string[pointer_index]
            if element_char != ",":
                auxiliary_characters.append(element_char)
            else:
                auxiliary_characters.append(" ")
            pointer_index += 1

        reconstructed_string = ""
        iterator_pos = 0
        while iterator_pos < len(auxiliary_characters):
            reconstructed_string += auxiliary_characters[iterator_pos]
            iterator_pos += 1

        result_words = reconstructed_string.split(" ")

    return result_words