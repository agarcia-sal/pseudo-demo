import re
from typing import List

def is_bored(input_string: str) -> int:
    def count_bored(n: int, sentences: List[str], total: int) -> int:
        if n >= len(sentences):
            return total
        current_sentence = sentences[n]
        increment = 1 if re.match(r'^I ', current_sentence) else 0
        return count_bored(n + 1, sentences, total + increment)

    fragments = re.split(r'[.?!]\s*', input_string)
    return count_bored(0, fragments, 0)