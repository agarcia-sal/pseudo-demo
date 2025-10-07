from typing import List

def parse_music(music_string: str) -> List[int]:
    durationLookup: dict[str, int] = {
        ".|": 1,
        "o|": 2,
        "o": 4
    }
    tokens: List[str] = music_string.split(" ")
    result: List[int] = []
    for token in tokens:
        if token != "":
            result.append(durationLookup[token])
    return result