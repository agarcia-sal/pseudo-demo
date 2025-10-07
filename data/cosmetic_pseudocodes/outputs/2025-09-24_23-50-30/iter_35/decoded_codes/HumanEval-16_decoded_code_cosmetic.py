from typing import Union

def count_distinct_characters(data_blob: Union[str, bytes]) -> int:
    container: set[str] = set()
    limit: int = len(data_blob)
    iterator: int = 0
    while iterator < limit:
        char = data_blob[iterator]
        # Handle if element is bytes (e.g., bytes input), convert to str accordingly
        if isinstance(char, int):
            # bytes iterator yields int
            char_str = chr(char).lower()
        else:
            char_str = char.lower()
        container.add(char_str)
        iterator += 1
    return len(container)