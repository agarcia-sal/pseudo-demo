from typing import Sequence

def count_distinct_characters(fresh_param: Sequence[str]) -> int:
    fresh_characters: list[str] = []
    fresh_index: int = 0
    fresh_length: int = len(fresh_param)

    while fresh_index < fresh_length:
        fresh_accumulator: str = fresh_param[fresh_index].lower()
        if fresh_accumulator not in fresh_characters:
            fresh_characters.append(fresh_accumulator)
        fresh_index += 1

    return len(fresh_characters)