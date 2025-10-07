from typing import List

def parse_music(music_string: str) -> List[int]:
    def get_duration(index: int, tokens_list: List[str], accum_list: List[int]) -> List[int]:
        if index >= len(tokens_list):
            return accum_list
        current_token = tokens_list[index]
        if current_token == '':
            return get_duration(index + 1, tokens_list, accum_list)
        durations_dict = {'o': 4, 'o|': 2, '.|': 1}
        return get_duration(index + 1, tokens_list, accum_list + [durations_dict[current_token]])

    return get_duration(0, music_string.split(" "), [])