from typing import List


def anti_shuffle(input_text: str) -> str:
    words_collection: List[str] = input_text.split(" ")
    ordered_words_container: List[str] = []
    index_counter: int = 0

    while index_counter < len(words_collection):
        current_token: str = words_collection[index_counter]
        characters_array: List[str] = list(current_token)
        sorted_array: List[str] = []

        while characters_array:
            smallest_char: str = characters_array[0]
            scan_index: int = 1
            while scan_index < len(characters_array):
                if characters_array[scan_index] < smallest_char:
                    smallest_char = characters_array[scan_index]
                scan_index += 1
            sorted_array.append(smallest_char)
            characters_array.remove(smallest_char)  # remove first occurrence

        assembled_word: str = ""
        for letter in sorted_array:
            assembled_word += letter
        ordered_words_container.append(assembled_word)
        index_counter += 1

    final_result: str = ""
    join_index: int = 0
    while join_index < len(ordered_words_container):
        final_result += ordered_words_container[join_index]
        if join_index < len(ordered_words_container) - 1:
            final_result += " "
        join_index += 1

    return final_result