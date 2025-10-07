from typing import List

def parse_music(music_string: str) -> List[int]:
    lengths_for_notes = {'o': 4, 'o|': 2, '.|': 1}
    results: List[int] = []
    tokens_iterator = iter(music_string.split(" "))

    while True:
        try:
            current_token = next(tokens_iterator)
        except StopIteration:
            break
        if current_token != "":
            results.append(lengths_for_notes[current_token])
    return results