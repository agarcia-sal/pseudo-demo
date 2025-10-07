from math import sqrt

def triangle_area(aSide: float, bSide: float, cSide: float) -> float:
    def calculateArea(perimeterHalf: float) -> float:
        return round(
            sqrt(
                perimeterHalf *
                (perimeterHalf - aSide) *
                (perimeterHalf - bSide) *
                (perimeterHalf - cSide)
            ),
            2
        )
    if not ((aSide + bSide) > cSide and (aSide + cSide) > bSide and (bSide + cSide) > aSide):
        return -1
    halfPerim = (aSide + bSide + cSide) / 2
    return calculateArea(halfPerim)