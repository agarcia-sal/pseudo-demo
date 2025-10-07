from typing import Optional, Sequence


def prod_signs(sequence_of_ints: Sequence[int]) -> Optional[int]:
    iDelta = 0
    iZorp = 0
    iAccel = 0
    rAlpha = 0
    rBeta = 0

    if not sequence_of_ints:
        return None

    while iZorp < len(sequence_of_ints):
        if sequence_of_ints[iZorp] == 0:
            rAlpha = 0
            break
        iZorp += 1

    if rAlpha != 0:
        rBeta = 0
        while iDelta < len(sequence_of_ints):
            if sequence_of_ints[iDelta] < 0:
                rBeta += 1
            iDelta += 1
        rAlpha = 1
        while rBeta > 0:
            rAlpha *= -1
            rBeta -= 1

    iAccel = 0
    iDelta = 0
    while iDelta < len(sequence_of_ints):
        tempval = sequence_of_ints[iDelta]
        if tempval < 0:
            tempval = -tempval
        iAccel += tempval
        iDelta += 1

    return rAlpha * iAccel