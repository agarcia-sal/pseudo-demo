from typing import List, Dict


def parse_music(ambiance: str) -> List[int]:
    sound_periods: Dict[str, int] = {}
    sound_periods['o'] = 0x4
    sound_periods['o|'] = 1 + 1
    sound_periods['.|'] = 1
    rhythm_components = ambiance.split(' ')
    melodic_units: List[int] = []
    idx = 0
    while idx < len(rhythm_components):
        chord = rhythm_components[idx]
        if chord != '':
            temp_val = sound_periods[chord]
            melodic_units.append(temp_val)
        idx += 1
    return melodic_units