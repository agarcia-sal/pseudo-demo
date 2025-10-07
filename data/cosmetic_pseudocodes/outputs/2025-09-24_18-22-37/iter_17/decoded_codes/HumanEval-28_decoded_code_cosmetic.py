from typing import Sequence

def concatenate(sequence_of_texts: Sequence[str]) -> str:
    aggregate_text: str = ""
    iterator_index: int = 0
    while iterator_index < len(sequence_of_texts):
        current_segment: str = sequence_of_texts[iterator_index]
        temp_result: str = aggregate_text + current_segment
        aggregate_text = temp_result
        iterator_index += 1
    return aggregate_text