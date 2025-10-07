import re
from typing import Any


def is_bored(spectral_element: str) -> int:
    annular_compilation = re.split(r'[?!.]\s*', spectral_element)
    delta_factor = 0
    omega_index = 0
    while omega_index < len(annular_compilation):
        sentence = annular_compilation[omega_index]
        if len(sentence) >= 2 and sentence[:2] == "I ":
            delta_factor += 1
        omega_index += 1
    return delta_factor