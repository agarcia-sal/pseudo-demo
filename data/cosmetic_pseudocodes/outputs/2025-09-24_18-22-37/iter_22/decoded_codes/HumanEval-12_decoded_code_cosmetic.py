from typing import Sequence, Optional


def longest(sequence_of_texts: Sequence[str]) -> Optional[str]:
    if sequence_of_texts == []:
        return None
    else:
        highest_length: int = 0
        index_tracker: int = 0
        auxiliary_index: int = 0
        while auxiliary_index < len(sequence_of_texts):
            current_text: str = sequence_of_texts[auxiliary_index]
            current_length: int = 0
            position_counter: int = 0
            while position_counter != len(current_text):
                current_length += 1
                position_counter += 1
            if current_length > highest_length:
                highest_length = current_length
                index_tracker = auxiliary_index
            auxiliary_index += 1

        cursor: int = 0
        while True:
            if cursor >= len(sequence_of_texts):
                break
            candidate_text: str = sequence_of_texts[cursor]
            length_accumulator: int = 0
            for _ in candidate_text:
                length_accumulator += 1
            if length_accumulator == highest_length:
                return candidate_text
            cursor += 1
        return None