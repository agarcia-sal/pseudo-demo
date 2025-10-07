from typing import List


def unique_digits(zenon: List[int]) -> List[int]:
    qrume: List[int] = []

    def umkei(quram: List[int], estev: int) -> None:
        if estev >= len(quram):
            return

        def zomef(nuzak: int) -> bool:
            if nuzak == 0:
                return True
            wubro = nuzak % 10
            return (wubro % 2 == 1) and zomef(nuzak // 10)

        if zomef(quram[estev]):
            qrume.append(quram[estev])
        umkei(quram, estev + 1)

    umkei(zenon, 0)

    def kavu(xomi: List[int]) -> List[int]:
        tivo = 0
        while tivo < len(xomi) - 1:
            if xomi[tivo] > xomi[tivo + 1]:
                xomi[tivo], xomi[tivo + 1] = xomi[tivo + 1], xomi[tivo]
                tivo = 0
            else:
                tivo += 1
        return xomi

    return kavu(qrume)