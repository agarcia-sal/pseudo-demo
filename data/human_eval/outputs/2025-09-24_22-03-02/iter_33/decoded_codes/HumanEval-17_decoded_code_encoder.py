def parse_music(music_string: str) -> list[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result_list = []
    split_list = music_string.split(' ')
    index = 0
    while index < len(split_list):
        current_element = split_list[index]
        if current_element != '':
            current_value = note_map[current_element]
            result_list.append(current_value)
        index += 1
    return result_list