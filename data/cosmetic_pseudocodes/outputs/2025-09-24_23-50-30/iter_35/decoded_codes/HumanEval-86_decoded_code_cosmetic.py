from typing import List

def anti_shuffle(input_string: str) -> str:
    array_items: List[str] = []
    temp_index: int = 0
    split_input: List[str] = input_string.split(" ")
    while temp_index < len(split_input):
        array_items.append(split_input[temp_index])
        temp_index += 1

    collected_results: List[str] = []
    idx_loop: int = 0
    while idx_loop < len(array_items):
        character_array: List[str] = []
        char_pos: int = 0
        current_word = array_items[idx_loop]
        while char_pos < len(current_word):
            character_array.append(current_word[char_pos])
            char_pos += 1

        asc_sorted_chars: List[str] = []
        while len(character_array) > 0:
            min_char: str = character_array[0]
            find_pos: int = 0
            look_pos: int = 1
            while look_pos < len(character_array):
                if character_array[look_pos] < min_char:
                    min_char = character_array[look_pos]
                    find_pos = look_pos
                look_pos += 1
            asc_sorted_chars.append(min_char)
            character_array.pop(find_pos)

        reconstructed_word: str = ""
        assemble_index: int = 0
        while assemble_index < len(asc_sorted_chars):
            reconstructed_word += asc_sorted_chars[assemble_index]
            assemble_index += 1

        collected_results.append(reconstructed_word)
        idx_loop += 1

    final_output: str = ""
    out_index: int = 0
    while out_index < len(collected_results):
        final_output += collected_results[out_index]
        if out_index < len(collected_results) - 1:
            final_output += " "
        out_index += 1

    return final_output