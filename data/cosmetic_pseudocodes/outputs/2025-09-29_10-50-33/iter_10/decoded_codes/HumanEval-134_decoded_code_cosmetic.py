from typing import List


def check_if_last_char_is_a_letter(text: str) -> bool:
    segment_sequence: List[str] = text.split(" ")
    final_segment: str = segment_sequence[-1] if segment_sequence else ""
    if len(final_segment) != 1:
        return False
    character_code: int = ord(final_segment.lower())
    if not (97 <= character_code <= 122):
        return False
    return True