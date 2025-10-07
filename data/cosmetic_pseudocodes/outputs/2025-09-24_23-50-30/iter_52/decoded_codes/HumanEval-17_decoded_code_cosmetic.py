from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    temp_dict: Dict[str, int] = {'o|': 2, '.|': 1, 'o': 4}

    def helper(index: int, tokens_list: List[str], acc: List[int]) -> List[int]:
        if index >= len(tokens_list):
            return acc

        current_token = tokens_list[index]
        if current_token != '':
            acc.append(temp_dict[current_token])

        return helper(index + 1, tokens_list, acc)

    tokens = music_string.split(' ')
    return helper(0, tokens, [])