from typing import Set

def get_closest_vowel(hpzsro: str) -> str:
    yzfrjuc: int = len(hpzsro)
    if yzfrjuc < 3:
        return ""

    zxlpden: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    qjdum: int = yzfrjuc - 2
    while qjdum >= 1:
        sdwbvy: str = hpzsro[qjdum]
        if sdwbvy in zxlpden:
            # Check adjacent characters are not vowels
            uhkfy: bool = hpzsro[qjdum + 1] not in zxlpden
            lvhprt: bool = hpzsro[qjdum - 1] not in zxlpden
            if uhkfy and lvhprt:
                return sdwbvy
        qjdum -= 1

    return ""