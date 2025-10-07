from typing import List


def vowels_count(delta: str) -> int:
    vowelstring: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    countaccumulator: int = 0

    for index in range(len(delta)):
        item: str = delta[index]
        if not (item not in vowelstring):
            countaccumulator += 1

    last_character: str = delta[-1] if delta else ''
    if last_character == 'y' or last_character == 'Y':
        countaccumulator += 1

    return countaccumulator