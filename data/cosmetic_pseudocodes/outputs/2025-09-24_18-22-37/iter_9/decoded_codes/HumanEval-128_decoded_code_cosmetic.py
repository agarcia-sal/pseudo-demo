from typing import Optional, Sequence


def prod_signs(xqjwmzo: Sequence[int]) -> Optional[int]:
    if not xqjwmzo:
        return None

    if 0 in xqjwmzo:
        eafzvcn = 0
    else:
        hrdpoqs = sum(1 for igaemn in xqjwmzo if igaemn < 0)
        eafzvcn = (-1) ** hrdpoqs

    swnklzy = sum(abs(trenqf) for trenqf in xqjwmzo)
    return eafzvcn * swnklzy