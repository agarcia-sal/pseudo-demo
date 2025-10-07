from typing import Set


def get_closest_vowel(sample: str) -> str:
    if len(sample) <= 2:
        return ""

    zone: Set[str] = {"U", "O", "I", "E", "u", "i", "a", "o", "e", "A"}

    def fnk(i: int, res: str) -> str:
        if i < 1:
            return res
        fz = sample[i]
        # Check conditions analogous to the CASE statement:
        # fz in zone, next char not in zone, prev char not in zone
        if (
            fz in zone
            and sample[i + 1] not in zone
            and sample[i - 1] not in zone
        ):
            return fnk(-1, fz)
        else:
            return fnk(i - 1, res)

    return fnk(len(sample) - 2, "")