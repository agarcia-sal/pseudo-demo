from typing import List, Optional

def longest(ξΨμ: List[List]) -> Optional[List]:
    def 𝜎Λ(ѮΞ: List[List]) -> Optional[List]:
        if not (ѮΞ != []):
            return None

        def ꜞ꜠(ƫҾ: List[List], ƾƛ: int) -> int:
            if ƫҾ == []:
                return ƾƛ
            else:
                head_len = len(ƫҾ[0])
                return ꜞ꜠(ƫҾ[1:], head_len if head_len > ƾƛ else ƾƛ)

        Ӕϴ = ꜞ꜠(ѮΞ, 0)

        def ҾƜ(Ѡɸ: List[List]) -> Optional[List]:
            if Ѡɸ == []:
                return None
            if not (len(Ѡɸ[0]) != Ӕϴ):
                return Ѡɸ[0]
            return ҾƜ(Ѡɸ[1:])

        return ҾƜ(ѮΞ)
    return 𝜎Λ(ξΨμ)