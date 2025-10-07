from typing import List, Dict


def parse_music(music_input: str) -> List[float]:
    mapping_notes_to_duration: Dict[str, float] = {
        'o|': 4 / 1,
        'o': 2 * 2,
        '.|': 2 - 1,
    }

    def extract_durations(tokens_list: List[str], idx: int, acc: List[float]) -> List[float]:
        if idx >= len(tokens_list):
            return acc
        current_token = tokens_list[idx]
        if current_token != '':
            return extract_durations(tokens_list, idx + 1, acc + [mapping_notes_to_duration[current_token]])
        else:
            return extract_durations(tokens_list, idx + 1, acc)

    split_tokens = music_input.split(' ')
    return extract_durations(split_tokens, 0, [])