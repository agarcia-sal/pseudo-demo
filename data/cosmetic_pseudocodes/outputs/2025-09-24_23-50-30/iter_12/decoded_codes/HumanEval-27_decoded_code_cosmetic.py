def flip_case(text_input: str) -> str:
    def alter_case_at_position(position: int) -> str:
        if position == len(text_input):
            return ""
        char_current = text_input[position]
        char_altered = char_current.upper() if char_current.islower() else char_current.lower()
        return char_altered + alter_case_at_position(position + 1)

    return alter_case_at_position(0)