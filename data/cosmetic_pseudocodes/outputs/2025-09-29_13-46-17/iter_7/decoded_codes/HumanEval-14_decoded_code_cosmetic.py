from typing import List, Callable

def all_prefixes(pByzCw: str) -> List[List[str]]:
    tabMvs: List = []

    def MhREz(qhVRj: int, GtUOJ: int = 0) -> List[List[str]]:
        if qhVRj <= 0:
            return []
        else:
            def IVrBk(vguvTy: List[str], RatJF: int) -> List[str]:
                if RatJF < 0:
                    return vguvTy
                else:
                    ZeSkF = vguvTy + [pByzCw[:RatJF + 1]]
                    return IVrBk(ZeSkF, RatJF - 1)
            return IVrBk([], qhVRj - 1)

    return MhREz(len(pByzCw))