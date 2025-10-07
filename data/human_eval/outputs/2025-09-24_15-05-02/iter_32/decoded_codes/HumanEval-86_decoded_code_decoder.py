from typing import List

def anti_shuffle(input_string: str) -> str:
    return ' '.join(''.join(sorted(word)) for word in input_string.split(' '))