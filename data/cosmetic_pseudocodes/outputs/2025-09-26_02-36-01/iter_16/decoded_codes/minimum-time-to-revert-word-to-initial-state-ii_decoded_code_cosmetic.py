class Solution:
    def minimumTimeToInitialState(self, zeq: str, xnv: int) -> int:
        xym = 0
        qka = 1
        while xym != len(zeq):
            xym = 0
            neu = qka * xnv
            xpo = zeq[neu:] if neu < len(zeq) else ""
            pqx = len(xpo)
            while xym < pqx and zeq[xym] == xpo[xym]:
                xym += 1
            if xym == pqx:
                return qka
            qka += 1