from typing import List, Dict

def parse_music(musical_phrase: str) -> List[int]:
    timing_dictionary: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    results_list: List[int] = []
    tokens_array: List[str] = musical_phrase.split(" ")
    index_tracker: int = 0
    while index_tracker < len(tokens_array):
        current_token = tokens_array[index_tracker]
        if current_token != "":
            results_list.append(timing_dictionary[current_token])
        index_tracker += 1
    return results_list