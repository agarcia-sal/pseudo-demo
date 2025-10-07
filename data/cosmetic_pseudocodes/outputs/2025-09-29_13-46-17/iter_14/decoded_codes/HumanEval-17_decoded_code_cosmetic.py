from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    value_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def helper(n: int) -> List[int]:
        if n == 0:
            return []
        idx = n - 1
        # Split music_string by spaces and get the n-th last element's mapped value
        tokens = music_string.split()
        val = value_map.get(tokens[idx], 0) if idx < len(tokens) else 0
        rest = helper(idx)
        return [val] + rest if val != 0 else rest

    length = len(music_string.split())
    return helper(length)