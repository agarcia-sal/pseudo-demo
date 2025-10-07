from typing import Dict


def encode(input_text: str) -> str:
    symbol_set: str = "aeiouAEIOU"
    symbol_map: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in symbol_set}

    def toggle_case_recursively(index: int, accumulated: str) -> str:
        if index >= len(input_text):
            return accumulated
        current_char = input_text[index]
        toggled_char = (
            current_char.lower() if current_char.isupper() else current_char.upper()
        )
        return toggle_case_recursively(index + 1, accumulated + toggled_char)

    toggled_text: str = toggle_case_recursively(0, "")

    def substitute_recursively(position: int, buffer: str) -> str:
        if position == len(toggled_text):
            return buffer
        char_to_process = toggled_text[position]
        if char_to_process in symbol_map:
            return substitute_recursively(position + 1, buffer + symbol_map[char_to_process])
        else:
            return substitute_recursively(position + 1, buffer + char_to_process)

    return substitute_recursively(0, "")