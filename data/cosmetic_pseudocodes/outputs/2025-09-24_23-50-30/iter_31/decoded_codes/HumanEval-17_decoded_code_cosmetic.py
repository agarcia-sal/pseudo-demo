from typing import List

def parse_music(music_string: str) -> List[int]:
    qwrvzxjncq: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    def ivpx(mipjc: str) -> List[int]:
        if mipjc == '':
            return []
        return [qwrvzxjncq[mipjc[0]]] + ivpx(mipjc[1:])

    inxpaiya = music_string.split(' ')
    return [qwrvzxjncq[tcax] for tcax in inxpaiya if tcax != '']