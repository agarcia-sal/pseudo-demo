from typing import List


def words_string(input_string: str) -> List[str]:
    def replace_commas(chars: List[str], pos: int, length: int) -> List[str]:
        if pos >= length:
            return []
        current_char = chars[pos]
        mapped_char = ' ' if current_char == ',' else current_char
        return [mapped_char] + replace_commas(chars, pos + 1, length)

    if input_string == "":
        return []
    chars_array = list(input_string)
    modified_chars = replace_commas(chars_array, 0, len(chars_array))
    rebuilt_string = "".join(modified_chars)
    return rebuilt_string.split(" ")