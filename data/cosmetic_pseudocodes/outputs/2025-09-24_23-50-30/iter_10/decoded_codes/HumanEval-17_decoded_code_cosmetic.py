from typing import List, Dict

def parse_music(input_sequence: str) -> List[int]:
    translate_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def helper(index: int, accumulated: List[int]) -> List[int]:
        tokens = input_sequence.split(' ')
        if index >= len(tokens):
            return accumulated
        current_token = tokens[index]
        if current_token != '':
            accumulated.append(translate_map[current_token])
        return helper(index + 1, accumulated)

    return helper(0, [])