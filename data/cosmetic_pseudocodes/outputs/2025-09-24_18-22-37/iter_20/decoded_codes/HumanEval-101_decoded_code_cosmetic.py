from typing import List


def words_string(parameter_string: str) -> List[str]:
    if parameter_string == "":
        return []

    temp_char_list: List[str] = []

    index_counter: int = 0
    while index_counter < len(parameter_string):
        current_char: str = parameter_string[index_counter]
        if current_char == ",":
            temp_char_list.append(" ")
        else:
            temp_char_list.append(current_char)
        index_counter += 1

    combined_string: str = ""
    pos: int = 0
    while pos < len(temp_char_list):
        combined_string += temp_char_list[pos]
        pos += 1

    result_words: List[str] = []
    word_start: int = 0

    while word_start < len(combined_string):
        while word_start < len(combined_string) and combined_string[word_start] == " ":
            word_start += 1
        if word_start >= len(combined_string):
            break

        word_end: int = word_start
        while word_end < len(combined_string) and combined_string[word_end] != " ":
            word_end += 1

        extracted_word: str = ""
        char_index: int = word_start
        while char_index < word_end:
            extracted_word += combined_string[char_index]
            char_index += 1

        result_words.append(extracted_word)
        word_start = word_end

    return result_words