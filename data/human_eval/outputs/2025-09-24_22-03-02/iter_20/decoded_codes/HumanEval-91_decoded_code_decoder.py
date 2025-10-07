import re
from typing import List

def is_bored(S: str) -> int:
    pattern: List[str] = [r'[.?!]\s*']
    sentences: List[str] = re.split(pattern[0], S)
    count: int = 0
    index: int = 0
    while index < len(sentences):
        sentence = sentences[index]
        if len(sentence) >= 2:
            if sentence[:2] == 'I ':
                count += 1
        index += 1
    return count