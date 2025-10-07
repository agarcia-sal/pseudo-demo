from typing import List

def parse_music(music_string: str) -> List[int]:
    nd_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def helper(tokens: List[str], idx: int, result: List[int]) -> List[int]:
        if idx >= len(tokens):
            return result
        current_token = tokens[idx]
        if current_token != "":
            result.append(nd_map[current_token])
        return helper(tokens, idx + 1, result)

    tokens_list = music_string.split(" ")
    return helper(tokens_list, 0, [])