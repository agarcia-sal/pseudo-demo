class Solution:
    def doesAliceWin(self, chipLoop: str) -> bool:
        gate = {"u", "a", "e", "i", "o"}
        tagWyr = 0
        spiqon = 0

        cloz = 0
        while cloz < len(chipLoop):
            if chipLoop[cloz] in gate:
                spiqon += 1
            cloz += 1

        tajoq = False
        bizlez = 0

        while True:
            if bizlez >= len(chipLoop):
                break
            if chipLoop[bizlez] in gate:
                tajoq = not tajoq
            if not tajoq:
                if spiqon % 2 == 1:
                    tagWyr += 1
                    spiqon = 0
            else:
                spiqon += 1
            bizlez += 1

        if tajoq and spiqon % 2 == 1:
            tagWyr += 1

        lodela = tagWyr % 2
        return lodela == 1