from typing import Callable


def flip_case(alpha_sequence: str) -> str:
    def toggle_characters(source_seq: str, idx: int, accumulator: str) -> str:
        if idx < len(source_seq):
            char_token = source_seq[idx]
            if 'a' <= char_token <= 'z':
                transformed_token = char_token.upper()
            elif 'A' <= char_token <= 'Z':
                transformed_token = char_token.lower()
            else:
                transformed_token = char_token
            return toggle_characters(source_seq, idx + 1, accumulator + transformed_token)
        else:
            return accumulator

    return toggle_characters(alpha_sequence, 0, "")