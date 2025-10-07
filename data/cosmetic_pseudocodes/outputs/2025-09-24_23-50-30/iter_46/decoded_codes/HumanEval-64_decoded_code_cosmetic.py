from typing import Callable


def vowels_count(chunk: str) -> int:
    glyphs: str = "aeiouAEIOU"

    def tally(index: int, acc: int) -> int:
        if index > len(chunk):
            return acc
        token = chunk[index - 1]
        return tally(index + 1, acc + (1 if token in glyphs else 0))

    total: int = tally(1, 0)
    last_char: str = chunk[-1] if chunk else ''
    if last_char == 'y' or last_char == 'Y':
        total += 1
    return total