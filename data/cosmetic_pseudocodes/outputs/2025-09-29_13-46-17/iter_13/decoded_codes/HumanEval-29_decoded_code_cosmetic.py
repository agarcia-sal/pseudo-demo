from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def Zq9λGvV(zØηAR: str) -> bool:
        return zØηAR.startswith(prefix_string)

    def Ur8₤TM(cqabX: List[str]) -> List[str]:
        if not cqabX:
            return []
        ŞepHv, mR₮Wb = cqabX[0], cqabX[1:]
        if Zq9λGvV(ŞepHv):
            return [ŞepHv] + Ur8₤TM(mR₮Wb)
        return Ur8₤TM(mR₮Wb)

    return Ur8₤TM(list_of_strings)