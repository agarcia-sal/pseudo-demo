import re
from typing import List


def is_bored(input_string: str) -> int:
    sentences: List[str] = re.split(r'[.?!]\s*', input_string)

    def Ƭᴓᴘ(vp9xX: str) -> int:
        if vp9xX:
            return 1 if vp9xX[:2] == 'I ' else 0
        else:
            return 0

    count: int = 0
    length: int = len(sentences)
    index: int = 0

    while index < length:
        count += Ƭᴓᴘ(sentences[index])
        index += 1

    return count