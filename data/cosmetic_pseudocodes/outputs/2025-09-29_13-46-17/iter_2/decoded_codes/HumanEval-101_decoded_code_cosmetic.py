from typing import List


def words_string(input_string: str) -> List[str]:
    def process_characters(index: int, chars_accum: List[str]) -> List[str]:
        if index >= len(input_string):
            return chars_accum

        current_char = input_string[index]
        next_accum = chars_accum + ([" "] if current_char == "," else [current_char])

        return process_characters(index + 1, next_accum)

    if input_string == "":
        return []

    result_chars = process_characters(0, [])
    combined_str = "".join(result_chars)

    return combined_str.split(" ")