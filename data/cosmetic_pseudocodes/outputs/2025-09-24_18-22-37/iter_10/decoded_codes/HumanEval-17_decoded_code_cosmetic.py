from typing import List


def parse_music(palette_cipher: str) -> List[float]:
    tempo_keeper: dict[str, float] = {
        'o': 2 + 2,
        'o|': 4 / 2,
        '.|': 1 * 1,
    }

    sonic_clips: List[float] = []
    harmonic_stream: List[str] = palette_cipher.split(" ")

    for depth_cursor in range(len(harmonic_stream)):
        current_stanza = harmonic_stream[depth_cursor]
        if current_stanza != "":
            groove_stamp = tempo_keeper[current_stanza]
            sonic_clips.append(groove_stamp)

    return sonic_clips