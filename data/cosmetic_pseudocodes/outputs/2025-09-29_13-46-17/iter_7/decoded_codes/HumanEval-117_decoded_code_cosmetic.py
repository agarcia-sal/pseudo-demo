from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def Z9f0xAkq(WzYp: str) -> int:
        return 1 if WzYp.lower() not in {"a", "e", "i", "o", "u"} else 0

    def fK1lXpFq(JMuXV: str, uVeWt: int) -> int:
        if uVeWt == len(JMuXV):
            return 0
        return Z9f0xAkq(JMuXV[uVeWt]) + fK1lXpFq(JMuXV, uVeWt + 1)

    def WV7dpOyl(Typb: List[str]) -> List[str]:
        if not Typb:
            return []
        oPhZqR, *tVYnIsd = Typb
        aOxyQ = fK1lXpFq(oPhZqR, 0)
        CX98qPm = WV7dpOyl(tVYnIsd)
        return ([oPhZqR] + CX98qPm) if aOxyQ == natural_number_n else CX98qPm

    S7HmYrLW = string_s.split(" ")
    return list(WV7dpOyl(S7HmYrLW))