from typing import List


def find_max(words_collection: List[str]) -> str:
    index_counter: int = 0
    maximized_word_container: List[tuple[int, str]] = []

    while index_counter < len(words_collection):
        current_entry: str = words_collection[index_counter]
        unique_chars_list: List[str] = []
        position_tracker: int = 0

        while position_tracker < len(current_entry):
            character_to_check: str = current_entry[position_tracker]
            if character_to_check not in unique_chars_list:
                unique_chars_list.append(character_to_check)
            position_tracker += 1

        maximized_word_container.append((-len(unique_chars_list), current_entry))
        index_counter += 1

    ii: int = 0
    while ii < len(maximized_word_container) - 1:
        ij: int = ii + 1
        while ij < len(maximized_word_container):
            if maximized_word_container[ij][0] < maximized_word_container[ii][0]:
                maximized_word_container[ii], maximized_word_container[ij] = (
                    maximized_word_container[ij],
                    maximized_word_container[ii],
                )
            elif (maximized_word_container[ij][0] == maximized_word_container[ii][0]
                  and not (maximized_word_container[ij][1] >= maximized_word_container[ii][1])):
                maximized_word_container[ii], maximized_word_container[ij] = (
                    maximized_word_container[ij],
                    maximized_word_container[ii],
                )
            ij += 1
        ii += 1

    return maximized_word_container[0][1]