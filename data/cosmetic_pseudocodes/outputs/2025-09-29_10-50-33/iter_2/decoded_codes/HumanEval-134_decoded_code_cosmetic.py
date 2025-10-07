from typing import List


def check_if_last_char_is_a_letter(text: str) -> bool:
    segments: List[str] = text.split(" ")
    final_piece: str = segments[-1] if segments else ""
    if len(final_piece) == 1:
        char_code: int = ord(final_piece.lower())
        if 97 <= char_code <= 122:
            return True
        else:
            return False
    else:
        return False