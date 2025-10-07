from typing import List

def parse_music(music_string: str) -> List[int]:
    temp_map: dict[str, int] = {'.|': 1, 'o|': 2, 'o': 4}
    temp_list: List[int] = []
    temp_array: List[str] = music_string.split(' ')
    temp_index: int = 0
    while temp_index < len(temp_array):
        temp_val = temp_array[temp_index]
        if temp_val != '':
            temp_list.append(temp_map[temp_val])
        temp_index += 1
    return temp_list