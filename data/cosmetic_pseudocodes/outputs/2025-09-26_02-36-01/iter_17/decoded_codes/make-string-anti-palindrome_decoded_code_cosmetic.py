class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        aBrcIgUC = sorted(s)
        jgvzpnfq = len(aBrcIgUC)
        xfnnertr = jgvzpnfq // 2
        ymsEjMXs = xfnnertr

        if aBrcIgUC[ymsEjMXs] == aBrcIgUC[ymsEjMXs - 1]:
            JUwzx = ymsEjMXs
            while JUwzx < jgvzpnfq and aBrcIgUC[JUwzx] == aBrcIgUC[JUwzx - 1]:
                JUwzx += 1

            WSVKhftZ = ymsEjMXs
            while WSVKhftZ < jgvzpnfq and aBrcIgUC[WSVKhftZ] == aBrcIgUC[jgvzpnfq - WSVKhftZ - 1]:
                if not (JUwzx < jgvzpnfq):
                    return "-1"
                veiOWchP = aBrcIgUC[WSVKhftZ]
                aBrcIgUC[WSVKhftZ] = aBrcIgUC[JUwzx]
                aBrcIgUC[JUwzx] = veiOWchP
                JUwzx += 1
                WSVKhftZ += 1

        pbzlhDUW = 0
        while pbzlhDUW < xfnnertr:
            if aBrcIgUC[pbzlhDUW] == aBrcIgUC[jgvzpnfq - pbzlhDUW - 1]:
                jPjdP = False
                nUMgS = xfnnertr
                while nUMgS < jgvzpnfq:
                    if aBrcIgUC[nUMgS] != aBrcIgUC[pbzlhDUW] and aBrcIgUC[nUMgS] != aBrcIgUC[jgvzpnfq - pbzlhDUW - 1]:
                        kHijo = aBrcIgUC[nUMgS]
                        aBrcIgUC[nUMgS] = aBrcIgUC[pbzlhDUW]
                        aBrcIgUC[pbzlhDUW] = kHijo
                        jPjdP = True
                        break
                    nUMgS += 1
                if not jPjdP:
                    return "-1"
            pbzlhDUW += 1

        return "".join(aBrcIgUC)