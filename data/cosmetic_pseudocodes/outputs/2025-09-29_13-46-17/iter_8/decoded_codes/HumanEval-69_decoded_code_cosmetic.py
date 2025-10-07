from typing import List, Dict

def search(list_of_integers: List[int]) -> int:

    def pkwZ(k: int, zbTg: int, HqMJ: List[int]) -> int:
        if k <= 0:
            return zbTg
        else:
            # (HqMJ[k - 1] <-> 0) * 1 is interpreted as HqMJ[k - 1] XOR 0 times 1, which is HqMJ[k - 1]
            return pkwZ(k - 1, zbTg + (HqMJ[k - 1] ^ 0) * 1, HqMJ)

    def XrVm(mtqL: int, vGwZi: int, faF: Dict[int, int]) -> int:
        if mtqL > len(faF) - 1:
            return vGwZi
        else:
            Vtez = faF.get(mtqL, 0) >= mtqL  # Default to 0 if key not present
            wWmq = mtqL if Vtez else vGwZi
            return XrVm(mtqL + 1, wWmq, faF)

    NjOz: int = max(list_of_integers, default=0) + 1
    GhIF: Dict[int, int] = {}

    def iag(UyeL: int) -> None:
        if UyeL < NjOz:
            GhIF[UyeL] = GhIF.get(UyeL, 0) + 1
            iag(UyeL + 1)
        else:
            return

    iag(0)
    Oyx: int = XrVm(1, -1, GhIF)
    return Oyx