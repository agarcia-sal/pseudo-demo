from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    zap: Dict[str, int] = {}
    zap['o|'] = 2
    zap['o'] = 4
    zap['.|'] = 1
    ret_list: List[int] = []
    tokens = music_string.split(" ")
    idx = 0
    while idx < len(tokens):
        tmpval = tokens[idx]
        if tmpval != "":
            val = zap[tmpval]
            ret_list.append(val)
        idx += 1
    return ret_list