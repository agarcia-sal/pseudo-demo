from typing import List, Dict

def parse_music(text_sequence: str) -> List[int]:
    temp_dictionary: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def helper(remaining_list: List[str], accumulated_list: List[int]) -> List[int]:
        if not remaining_list:
            return accumulated_list
        current_element = remaining_list[0]
        tail_list = remaining_list[1:]
        if current_element == '':
            return helper(tail_list, accumulated_list)
        return helper(tail_list, accumulated_list + [temp_dictionary[current_element]])

    split_sequence = text_sequence.split(' ')
    return helper(split_sequence, [])