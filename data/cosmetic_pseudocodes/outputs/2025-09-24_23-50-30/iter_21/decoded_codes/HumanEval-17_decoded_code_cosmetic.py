from collections import deque
from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    mapping_dict: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    tokens_queue: deque[str] = deque(
        char_array for char_array in music_string.split(' ') if char_array
    )

    result_list: List[int] = []
    while tokens_queue:
        current_token = tokens_queue.popleft()
        result_list.append(mapping_dict[current_token])

    return result_list