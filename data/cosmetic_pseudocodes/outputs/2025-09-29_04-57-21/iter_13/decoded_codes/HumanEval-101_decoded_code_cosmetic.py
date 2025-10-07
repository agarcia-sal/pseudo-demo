from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    processed_chars: List[str] = []

    def process_chars_at(index: int) -> None:
        if index >= len(input_string):
            return
        current_char = input_string[index]
        if current_char == ",":
            processed_chars.append(" ")
        else:
            processed_chars.append(current_char)
        process_chars_at(index + 1)

    process_chars_at(0)

    combined_str = "".join(processed_chars)
    return combined_str.split()