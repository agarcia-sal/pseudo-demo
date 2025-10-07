from typing import List

def parse_music(melody_text: str) -> List[int]:
    time_values: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    # Filter out empty tokens and map each to its corresponding time value
    return [time_values[token] for token in melody_text.split(' ') if token != '']