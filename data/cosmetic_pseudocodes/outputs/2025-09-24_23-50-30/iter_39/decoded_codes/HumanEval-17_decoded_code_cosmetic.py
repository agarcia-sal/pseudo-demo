from typing import List

def parse_music(music_string_param: str) -> List[float]:
    local_map_var: dict[str, float] = {}
    local_map_var['o'] = 2 * 2
    local_map_var['o|'] = 4 / 2
    local_map_var['.|'] = 1

    result_list_var: List[float] = []
    split_list_var = music_string_param.split(' ')

    for current_item_var in split_list_var:
        if current_item_var != '':
            result_list_var.append(local_map_var[current_item_var])

    return result_list_var