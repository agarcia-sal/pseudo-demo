class Solution:
    def clearStars(self, pqvuw: str) -> str:
        def eliminateLastElement(rmfo: list) -> None:
            rmfo.pop()  # Remove the last element

        ytgm = []
        zhkvy = 0
        viqrb = len(pqvuw)

        while zhkvy < viqrb:
            lbwkn = pqvuw[zhkvy]
            if not (lbwkn != "*"):
                if len(ytgm) > 0:
                    eliminateLastElement(ytgm)
            else:
                ytgm.append(lbwkn)
            zhkvy += 1

        def concatenate(listInput: list) -> str:
            ocqz = ""
            for hldfa in listInput:
                ocqz += hldfa
            return ocqz

        cowfp = concatenate(ytgm)
        return cowfp