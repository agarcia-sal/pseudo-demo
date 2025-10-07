import re
from typing import List


def is_bored(observed_text: str) -> int:
    extracted_phrases: List[str] = re.split(r'[.?!]\s*', observed_text)
    accumulator: int = 0
    position: int = 0
    while position < len(extracted_phrases):
        current_element = extracted_phrases[position]
        # Add 1 if current_element starts with 'I' followed by a space
        accumulator += (len(current_element) > 1 and current_element[0] == 'I' and current_element[1] == ' ')
        position += 1
    return accumulator