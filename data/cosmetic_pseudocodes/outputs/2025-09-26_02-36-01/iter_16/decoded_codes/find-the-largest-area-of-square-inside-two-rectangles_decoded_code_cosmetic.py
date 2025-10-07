class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            xA = bl1[0]
            xB = bl2[0]
            cLeft = xA if xA >= xB else xB

            yA = bl1[1]
            yB = bl2[1]
            dBottom = yA if yA >= yB else yB

            xC = tr1[0]
            xD = tr2[0]
            eRight = xC if xC <= xD else xD

            yC = tr1[1]
            yD = tr2[1]
            fTop = yC if yC <= yD else yD

            if cLeft >= eRight or dBottom >= fTop:
                return 0

            gWidth = eRight - cLeft
            hHeight = fTop - dBottom
            jSide = gWidth if gWidth <= hHeight else hHeight

            return jSide * jSide

        vMaxArea = 0
        zLen = len(bottomLeft)
        xIndex = 0
        while xIndex < zLen:
            yIndex = xIndex + 1
            while yIndex < zLen:
                qCandidate = intersecting_square_area(bottomLeft[xIndex], topRight[xIndex], bottomLeft[yIndex], topRight[yIndex])
                if vMaxArea < qCandidate:
                    vMaxArea = qCandidate
                yIndex += 1
            xIndex += 1
        return vMaxArea