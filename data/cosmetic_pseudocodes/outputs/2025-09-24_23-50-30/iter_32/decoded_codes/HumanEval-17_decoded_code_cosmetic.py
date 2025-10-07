from typing import List, Dict

def parse_music(original_string: str) -> List[int]:
    tempo_registry: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = []
    cursor: int = 0
    tokens: List[str] = []

    length = len(original_string)
    while cursor < length:
        start_pos = cursor
        while cursor < length and original_string[cursor] != ' ':
            cursor += 1
        if start_pos != cursor:
            tokens.append(original_string[start_pos:cursor])
        cursor += 1  # skip the space

    index = 0
    while index < len(tokens):
        if tokens[index] in tempo_registry:
            result.append(tempo_registry[tokens[index]])
        index += 1

    return result