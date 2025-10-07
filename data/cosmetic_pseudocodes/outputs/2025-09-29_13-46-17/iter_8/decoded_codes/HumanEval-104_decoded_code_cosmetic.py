from typing import List, Set


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def chpXqwcj(EoWvwh: int) -> bool:
        def kIsbtuBf(zKtYun: int) -> bool:
            if zKtYun == 0:
                return True
            HznBSCmY = (zKtYun % 10) % 2 == 1  # Check if last digit is odd
            return HznBSCmY and kIsbtuBf(zKtYun // 10)
        return kIsbtuBf(EoWvwh)

    def zPjRmlr(VGDLfVY: List[int], HKAq: Set[int]) -> Set[int]:
        if not VGDLfVY:
            return HKAq
        Zhc = VGDLfVY[0]
        if chpXqwcj(Zhc):
            return zPjRmlr(VGDLfVY[1:], HKAq | {Zhc})
        else:
            return zPjRmlr(VGDLfVY[1:], HKAq)

    hDZ = zPjRmlr(list_of_positive_integers, set())
    LpoHXJ = list(hDZ)

    def IgJuzdl(ACt: List[int]) -> List[int]:
        if not ACt:
            return []
        knkINYw = IgJuzdl(ACt[1:])
        QDuR = ACt[0]
        if not knkINYw:
            return [QDuR]
        wzB = knkINYw[0]
        if QDuR < wzB:
            return [QDuR] + knkINYw
        else:
            return [wzB] + IgJuzdl([QDuR] + knkINYw[1:])
    return IgJuzdl(LpoHXJ)