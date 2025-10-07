def flip_case(source_text: str) -> str:
    def toggle_character(index: int, accumulator: str) -> str:
        if index >= len(source_text):
            return accumulator
        current_char = source_text[index]
        is_upper = 'A' <= current_char <= 'Z'
        new_char = current_char.lower() if is_upper else current_char.upper()
        return toggle_character(index + 1, accumulator + new_char)

    return toggle_character(0, "")