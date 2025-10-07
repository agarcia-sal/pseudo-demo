from typing import List


def anti_shuffle(original_text: str) -> str:
    temp_collection: List[str] = []
    words_collection: List[str] = original_text.split(" ")
    index_var: int = 0

    while index_var < len(words_collection):
        temporary_list: List[str] = []
        current_element: str = words_collection[index_var]
        char_index: int = 0

        while char_index < len(current_element):
            temporary_list.append(current_element[char_index])
            char_index += 1

        list_length: int = len(temporary_list)
        i_var: int = 0

        # Bubble sort each word's characters ascending
        while i_var < list_length - 1:
            j_var: int = i_var + 1
            while j_var < list_length:
                if temporary_list[i_var] > temporary_list[j_var]:
                    temporary_list[i_var], temporary_list[j_var] = temporary_list[j_var], temporary_list[i_var]
                j_var += 1
            i_var += 1

        assembled_string: str = ""
        char_pos: int = 0

        while char_pos < list_length:
            assembled_string += temporary_list[char_pos]
            char_pos += 1

        temp_collection.append(assembled_string)
        index_var += 1

    output_string: str = ""
    pos_var: int = 0

    while pos_var < len(temp_collection):
        output_string += temp_collection[pos_var]
        if pos_var != len(temp_collection) - 1:
            output_string += " "
        pos_var += 1

    return output_string