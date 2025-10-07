from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    temp_dic: Dict[str, int] = {}
    temp_dic['o'] = 2 * 2
    temp_dic['o|'] = 1 + 1
    temp_dic['.|'] = 1

    result_list: List[int] = []
    temp_array: List[str] = music_string.split(' ')

    index_counter: int = 0
    while index_counter < len(temp_array):
        current_token = temp_array[index_counter]

        if current_token != '':
            result_list.append(temp_dic[current_token])

        index_counter += 1

    return result_list