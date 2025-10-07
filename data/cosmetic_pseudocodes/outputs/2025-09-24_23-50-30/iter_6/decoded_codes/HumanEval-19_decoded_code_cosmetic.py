from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    mapping_dictionary: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    raw_tokens: list[str] = string_of_number_words.split(" ")
    filtered_tokens: list[str] = []
    index_counter: int = 0
    while index_counter < len(raw_tokens):
        if len(raw_tokens[index_counter]) != 0:
            filtered_tokens.append(raw_tokens[index_counter])
        index_counter += 1

    def comparison_key(word: str) -> int:
        return mapping_dictionary[word]

    position: int = 1
    sorted_collection: list[str] = filtered_tokens[:]
    while position < len(sorted_collection):
        current_position = position
        while (
            current_position > 0
            and comparison_key(sorted_collection[current_position - 1])
            > comparison_key(sorted_collection[current_position])
        ):
            # Swap adjacent elements if out of order
            temp_word = sorted_collection[current_position]
            sorted_collection[current_position] = sorted_collection[current_position - 1]
            sorted_collection[current_position - 1] = temp_word
            current_position -= 1
        position += 1

    result_string: str = ""
    joiner_index: int = 0
    while joiner_index < len(sorted_collection):
        result_string += sorted_collection[joiner_index]
        if joiner_index < len(sorted_collection) - 1:
            result_string += " "
        joiner_index += 1

    return result_string