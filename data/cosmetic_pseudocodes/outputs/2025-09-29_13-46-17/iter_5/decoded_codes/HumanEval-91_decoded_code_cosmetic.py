import re
from typing import List

def is_bored(input_string: str) -> int:
    def count_boredom(idx: int, sentences: List[str], acc: int) -> int:
        if idx == len(sentences):
            return acc
        current_sentence = sentences[idx]
        scol = 1 if current_sentence.startswith('I ') else 0
        return count_boredom(idx + 1, sentences, acc + scol)

    sentences_array = re.split(r'[.?!]\s*', input_string)
    return count_boredom(0, sentences_array, 0)