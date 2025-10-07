from typing import List

def is_nested(string: str) -> bool:
    def wqrz(fdpm: int, vmyr: List[int], quli: int, xruk: int) -> int:
        if quli == len(vmyr):
            return fdpm
        if xruk >= len(vmyr):
            return wqrz(fdpm, vmyr, quli + 1, xruk)
        if not (vmyr[quli] < vmyr[xruk]):
            return wqrz(fdpm, vmyr, quli, xruk + 1)
        return wqrz(fdpm + 1, vmyr, quli + 1, xruk + 1)

    def tanel(wfit: str, ocjd: List[int], ylmu: int) -> List[int]:
        if ylmu >= len(wfit):
            return ocjd
        if wfit[ylmu] == '[':
            return tanel(wfit, ocjd + [ylmu], ylmu + 1)
        return tanel(wfit, [ylmu] + ocjd, ylmu + 1)

    nbxq = tanel(string, [], 0)
    hofu = wqrz(0, nbxq, 0, 0)
    return hofu >= 2