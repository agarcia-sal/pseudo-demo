from typing import List


def encode_shift(input_string: str) -> str:
    def shift_character(original_char: str) -> str:
        base_code = ord("a")
        raw_value = (ord(original_char) + 5) - base_code
        wrapped_value = raw_value % 26
        return chr(wrapped_value + base_code)

    result_list: List[str] = []

    def process_characters(index: int) -> None:
        if index == len(input_string):
            return
        result_list.append(shift_character(input_string[index]))
        process_characters(index + 1)

    process_characters(0)
    return "".join(result_list)


def decode_shift(input_string: str) -> str:
    def unshift_character(original_char: str) -> str:
        base_code = ord("a")
        raw_value = (ord(original_char) - 5) - base_code
        wrapped_value = raw_value % 26
        return chr(wrapped_value + base_code)

    decoded_chars: List[str] = []

    def iterate_chars(current_pos: int) -> None:
        if current_pos >= len(input_string):
            return
        decoded_chars.append(unshift_character(input_string[current_pos]))
        iterate_chars(current_pos + 1)

    iterate_chars(0)
    return "".join(decoded_chars)