from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    mappingVar: Dict[str, int] = {
        '.|': 1,
        'o|': 2,
        'o': 4,
    }

    def helper_func(listVar: List[str], accList: List[int]) -> List[int]:
        if not listVar:
            return accList
        current: str = listVar[0]
        restList: List[str] = listVar[1:]
        if current != "":
            return helper_func(restList, accList + [mappingVar[current]])
        else:
            return helper_func(restList, accList)

    splitList: List[str] = music_string.split(" ")
    return helper_func(splitList, [])