from typing import Dict


def anti_shuffle(input_string: str) -> str:
    words_array: list[str] = input_string.split(" ")
    reordered_list: Dict[int, str] = {}
    index_counter: int = 0

    while index_counter < len(words_array):
        current_token: str = words_array[index_counter]
        char_sequence: list[str] = list(current_token)
        position_i: int = 0

        # Sort characters by repeatedly swapping smaller characters forward
        while position_i < len(char_sequence) - 1:
            position_j: int = position_i + 1
            while position_j < len(char_sequence):
                if char_sequence[position_i] > char_sequence[position_j]:
                    char_sequence[position_i], char_sequence[position_j] = (
                        char_sequence[position_j],
                        char_sequence[position_i],
                    )
                position_j += 1
            position_i += 1

        reordered_list[index_counter] = "".join(char_sequence)
        index_counter += 1

    assembled_string: str = ""
    pos_k: int = 0

    while pos_k < len(reordered_list):
        if pos_k == 0:
            assembled_string = reordered_list[pos_k]
        else:
            assembled_string = assembled_string + " " + reordered_list[pos_k]
        pos_k += 1

    return assembled_string