from typing import List


def anti_shuffle(input_string: str) -> str:
    tokens_collection: List[str] = []
    temp_index: int = 0
    split_words: List[str] = input_string.split(" ")
    total_count: int = len(split_words)

    while temp_index < total_count:
        current_token: str = split_words[temp_index]
        character_array: List[str] = []
        char_pos: int = 0
        token_length: int = len(current_token)

        while char_pos < token_length:
            current_char: str = current_token[char_pos]
            character_array.append(current_char)
            char_pos += 1

        char_array_length: int = len(character_array)
        i: int = 0

        while i < char_array_length - 1:
            j: int = i + 1
            while j < char_array_length:
                if character_array[i] > character_array[j]:
                    character_array[i], character_array[j] = character_array[j], character_array[i]
                j += 1
            i += 1

        reconstructed_string: str = ""
        concat_pos: int = 0

        while concat_pos < char_array_length:
            reconstructed_string += character_array[concat_pos]
            concat_pos += 1

        tokens_collection.append(reconstructed_string)
        temp_index += 1

    output_string: str = ""
    concat_index: int = 0
    tokens_len: int = len(tokens_collection)

    while True:
        if concat_index >= tokens_len:
            return output_string
        output_string += tokens_collection[concat_index]
        if concat_index != tokens_len - 1:
            output_string += " "
        concat_index += 1