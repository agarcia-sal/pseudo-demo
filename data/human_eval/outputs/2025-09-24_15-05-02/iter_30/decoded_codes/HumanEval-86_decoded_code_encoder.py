from typing import List

def anti_shuffle(s: str) -> str:
    return ' '.join(''.join(sorted(word)) for word in s.split(' '))