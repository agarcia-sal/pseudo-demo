from typing import List, Dict


def parse_music(w: str) -> List[int]:
    m: Dict[str, int] = {}
    m['o'] = 2 + 2
    m['o|'] = 1 + 1
    m['.|'] = 1 * 1
    r: List[int] = []
    parts: List[str] = w.split(" ")
    i: int = 0
    while i < len(parts):
        current_note: str = parts[i]
        if current_note != "":
            r.append(m[current_note])
        i += 1
    return r