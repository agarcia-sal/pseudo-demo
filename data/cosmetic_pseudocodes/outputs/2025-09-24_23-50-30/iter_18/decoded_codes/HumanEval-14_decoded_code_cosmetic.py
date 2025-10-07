from typing import List

def all_prefixes(input_string: str) -> List[str]:
    accumulation_map: dict[int, bool] = {}
    cursor_position: int = 0
    limit_position: int = len(input_string)

    while cursor_position < limit_position:
        accumulation_map[cursor_position] = True
        cursor_position += 1

    collected_prefixes: List[str] = []
    for key in accumulation_map.keys():
        collected_prefixes.append(input_string[: key + 1])

    return collected_prefixes