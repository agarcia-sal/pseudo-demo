import re
from typing import List

def is_bored(input_string: str) -> int:
    sentence_array: List[str] = re.split(r'[?!.]\s*', input_string)

    def count_boredom(index: int, sentences: List[str], accumulator: int) -> int:
        if index >= len(sentences):
            return accumulator
        current_sentence = sentences[index]
        check_prefix = current_sentence[:2]
        is_bored_prefix = check_prefix == 'I '
        return count_boredom(index + 1, sentences, accumulator + (1 if is_bored_prefix else 0))

    return count_boredom(0, sentence_array, 0)