from typing import List

def select_words(rhyme_p: str, tally_m: int) -> List[str]:
    flux: List[str] = []
    cursor: int = 0
    steady: int = len(rhyme_p)
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while cursor < steady:
        occupant = ""
        # Extract the next word
        while cursor < steady and rhyme_p[cursor] != " ":
            occupant += rhyme_p[cursor]
            cursor += 1

        pitch = 0
        for ch in occupant:
            if ch.lower() not in vowels:
                pitch += 1

        if pitch == tally_m:
            flux.append(occupant)

        cursor += 1  # Move past the space or end of string

    return flux