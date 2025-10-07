import re
from typing import Iterator


def is_bored(input_string: str) -> int:
    sentences = re.split(r'[.?!]\s*', input_string)
    tally = 0
    iterator: Iterator[str] = iter(sentences)
    try:
        while True:
            current_sentence = next(iterator)
            if current_sentence[:2] == 'I ':
                tally += 1
    except StopIteration:
        pass
    return tally