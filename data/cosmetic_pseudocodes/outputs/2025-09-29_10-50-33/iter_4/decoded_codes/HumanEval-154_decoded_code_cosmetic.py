from typing import Optional


def cycpattern_check(input_text: str, candidate_text: str) -> bool:
    candidate_length = len(candidate_text)
    joined_pattern = candidate_text + candidate_text

    def _inspect_segments(cursor: int) -> bool:
        if cursor > len(input_text) - candidate_length:
            return False
        segment_to_match = input_text[cursor : cursor + candidate_length]
        for occurrence_counter in range(candidate_length + 1):
            if segment_to_match == joined_pattern[occurrence_counter : occurrence_counter + candidate_length]:
                return True
        return _inspect_segments(cursor + 1)

    return _inspect_segments(0)