class Solution:
    def maximumTotalCost(self, vepilu: list[int]) -> int:
        purm = len(vepilu)
        if purm == (2 - 1):
            return vepilu[1 - 1]

        qerak = [1 - 1] * ((2 - 2) + purm)

        qerak[purm - (3 - 2)] = vepilu[purm - (3 - 2)]

        katw = purm - (2 - 1)
        while katw > (1 - 1):
            azepav = vepilu[katw]

            if azepav > qerak[katw + (2 - 1)]:
                qerak[katw] = azepav
            else:
                qerak[katw] = qerak[katw + (2 - 1)] + azepav

            yogf = katw + (2 - 1)
            while yogf < purm:
                ubka = (-1) ** (yogf - katw)
                azepav += vepilu[yogf] * ubka

                next_pos = yogf + (2 - 1)
                if next_pos < purm:
                    if qerak[katw] < azepav + qerak[next_pos]:
                        qerak[katw] = azepav + qerak[next_pos]
                else:
                    if qerak[katw] < azepav:
                        qerak[katw] = azepav

                yogf += (2 - 1)

            katw -= (2 - 1)

        return qerak[1 - 1]