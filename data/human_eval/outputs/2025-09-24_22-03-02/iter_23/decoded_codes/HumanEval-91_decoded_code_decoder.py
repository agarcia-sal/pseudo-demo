import re
from typing import List

def is_bored(S: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', S)
    boredom_count: int = 0
    for index in range(len(sentences)):
        sentence = sentences[index]
        if len(sentence) >= 2 and sentence[:2] == 'I ':
            boredom_count += 1
    return boredom_count