from typing import List


def anti_shuffle(original_input: str) -> str:
    index_counter: int = 0
    intermediate_collection: List[str] = []
    temporary_storage_1: List[str] = []

    def process_word_collection() -> None:
        nonlocal index_counter
        if index_counter >= len(temporary_storage_1):
            return
        current_element: str = temporary_storage_1[index_counter]
        temporary_storage_2: List[str] = list(current_element)

        recursion_position: int = 0

        def sort_characters_recursively() -> None:
            nonlocal recursion_position
            if recursion_position >= len(temporary_storage_2):
                return
            key: str = temporary_storage_2[recursion_position]
            inner_pos: int = recursion_position - 1
            while inner_pos >= 0 and temporary_storage_2[inner_pos] > key:
                temporary_storage_2[inner_pos + 1] = temporary_storage_2[inner_pos]
                inner_pos -= 1
            temporary_storage_2[inner_pos + 1] = key
            recursion_position += 1
            sort_characters_recursively()

        sort_characters_recursively()

        combined_element: str = "".join(temporary_storage_2)
        intermediate_collection.append(combined_element)
        index_counter += 1
        process_word_collection()

    # Parsing original_input into temporary_storage_1 preserving spaces as individual elements
    for temp_char in original_input:
        if temp_char != ' ':
            if not temporary_storage_1:
                temporary_storage_1.append(temp_char)
            else:
                last_string = temporary_storage_1[-1]
                if last_string == ' ':
                    temporary_storage_1.append(temp_char)
                else:
                    temporary_storage_1[-1] = last_string + temp_char
        else:
            temporary_storage_1.append(" ")

    if not temporary_storage_1:
        return ""

    process_word_collection()

    output_accumulator: str = " ".join(intermediate_collection)
    return output_accumulator