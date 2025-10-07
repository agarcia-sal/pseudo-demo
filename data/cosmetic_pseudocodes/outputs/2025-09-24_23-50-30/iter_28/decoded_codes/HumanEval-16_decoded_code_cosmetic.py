from typing import Sequence

def count_distinct_characters(data_chunk: Sequence[str]) -> int:
    char_pool: list[str] = []
    unique_bucket: set[str] = set()
    index: int = 0

    while index < len(data_chunk):
        current_unit = data_chunk[index].lower()
        if current_unit not in unique_bucket:
            char_pool.append(current_unit)
            unique_bucket.add(current_unit)
        index += 1

    return len(char_pool)