from typing import List


def words_string(original_text: str) -> List[str]:
    def transform_characters(index: int, accumulator: str) -> str:
        if index >= len(original_text):
            return accumulator

        current_char = original_text[index]
        updated_accumulator = accumulator + (' ' if current_char == ',' else current_char)
        return transform_characters(index + 1, updated_accumulator)

    if not original_text:
        return []

    replaced_string = transform_characters(0, "")
    split_result: List[str] = []
    start_pos = 0
    position = 0
    length = len(replaced_string)

    while position <= length:
        if position == length or replaced_string[position] == ' ':
            if position > start_pos:
                split_result.append(replaced_string[start_pos:position])
            start_pos = position + 1
        position += 1

    return split_result