from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    durations: Dict[str, int] = {'o': 4, '.|': 1, 'o|': 2}

    def accumulate_notes(notesList: List[str], idx: int, acc: List[int]) -> List[int]:
        if idx >= len(notesList):
            return acc
        currentNote = notesList[idx]
        if currentNote != '':
            acc.append(durations[currentNote])
        return accumulate_notes(notesList, idx + 1, acc)

    tokens = music_string.split(' ')
    return accumulate_notes(tokens, 0, [])