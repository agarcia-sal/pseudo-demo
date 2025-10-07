from typing import List, Dict

def parse_music(music_string_1: str) -> List[int]:
    mapping_1: Dict[str, int] = {'.|': 1, 'o|': 2, 'o': 4}
    tokens_1: List[str] = music_string_1.split(' ')

    def helper_1(index_1: int, acc_1: List[int]) -> List[int]:
        if index_1 >= len(tokens_1):
            return acc_1
        current_1 = tokens_1[index_1]
        return helper_1(index_1 + 1, acc_1 + [mapping_1[current_1]] if current_1 != '' else acc_1)

    return helper_1(0, [])