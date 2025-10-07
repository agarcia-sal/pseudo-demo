from typing import List

def switch_case(ch: str) -> str:
    if 'a' <= ch <= 'z':
        return chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':
        return chr(ord(ch) + 32)
    return ch  # fallback if character is non-alphabetic, though not expected per original logic

def concatenate_elements(list_of_chars: List[str]) -> str:
    # Join the list of characters into a string
    return ''.join(list_of_chars)

def reverse_string(s: str) -> str:
    # Return string reversed
    return s[::-1]

def solve(string_input: str) -> str:
    flag_indicator: bool = False
    position_counter: int = 0
    transformed_chars: List[str] = list(string_input)

    def convert_chars(pos: int) -> None:
        nonlocal flag_indicator
        if pos >= len(string_input):
            return
        current_char = string_input[pos]
        if ('A' <= current_char <= 'Z') or ('a' <= current_char <= 'z'):
            transformed_chars[pos] = switch_case(current_char)
            flag_indicator = True
        convert_chars(pos + 1)

    convert_chars(position_counter)

    aggregated_result = concatenate_elements(transformed_chars)

    if not flag_indicator:
        return reverse_string(aggregated_result)
    else:
        return aggregated_result