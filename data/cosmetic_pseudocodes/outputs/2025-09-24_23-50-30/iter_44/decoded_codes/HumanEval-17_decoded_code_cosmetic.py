from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_associations: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    syllable_list: List[str] = music_string.split(" ")
    filtered_syllables: List[str] = [syllable for syllable in syllable_list if len(syllable) > 0]
    transformed_durations: List[int] = [duration_associations[syllable] for syllable in filtered_syllables]
    return transformed_durations