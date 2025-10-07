from typing import List, Dict

def parse_music(sound_phrase: str) -> List[int]:
    timing_dictionary: Dict[str, int] = {
        'o|': 2,
        'o': 4,
        '.|': 1,
    }

    result_sequence: List[int] = []
    tokens: List[str] = sound_phrase.split(' ')

    index_var: int = 0
    while index_var < len(tokens):
        current_token: str = tokens[index_var]
        if current_token != '':
            result_sequence.append(timing_dictionary[current_token])
        index_var += 1

    return result_sequence