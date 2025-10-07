from typing import List


def anti_shuffle(input_string: str) -> str:
    word_collection: List[str] = input_string.split(" ")
    reordered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(word_collection):
        current_word: str = word_collection[index_counter]
        character_sequence: List[str] = list(current_word)
        sorted_sequence: List[str] = []
        char_index: int = 0

        while char_index < len(character_sequence):
            next_char: str = character_sequence[char_index]
            insertion_index: int = 0
            # Find insertion index to keep sorted_sequence sorted ascendingly
            while (insertion_index < len(sorted_sequence)
                   and not (next_char < sorted_sequence[insertion_index])):
                insertion_index += 1
            sorted_sequence.insert(insertion_index, next_char)
            char_index += 1

        temp_string: str = ""
        build_index: int = 0
        while build_index < len(sorted_sequence):
            temp_string += sorted_sequence[build_index]
            build_index += 1

        reordered_collection.append(temp_string)
        index_counter += 1

    final_output: str = ""
    join_cursor: int = 0
    while join_cursor < len(reordered_collection):
        final_output += reordered_collection[join_cursor]
        if join_cursor < len(reordered_collection) - 1:
            final_output += " "
        join_cursor += 1

    return final_output