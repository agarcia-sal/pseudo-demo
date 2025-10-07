class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(ch: str) -> bool:
            return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

        def toInt(ch: str) -> int:
            return ord(ch) - ord('0')

        def dictGet(d: dict, k: str) -> int:
            return d[k] if k in d else 0

        def dictSetAdd(d: dict, k: str, v: int) -> None:
            d[k] = dictGet(d, k) + v

        def sortAlphaKeys(d: dict) -> list:
            keysList = list(d.keys())

            def swap(a: int, b: int) -> None:
                keysList[a], keysList[b] = keysList[b], keysList[a]

            n = len(keysList)
            i = 0
            while i < n - 1:
                j = i + 1
                while j < n:
                    if not (keysList[i] <= keysList[j]):
                        swap(i, j)
                    j += 1
                i += 1
            return keysList

        xA1B = {}
        xI9J = ""
        n3K4 = 0

        iP = 0
        while iP < len(compressed):
            z7V = compressed[iP]
            if isAlpha(z7V):
                if xI9J != "":
                    dictSetAdd(xA1B, xI9J, n3K4)
                xI9J = z7V
                n3K4 = 0
            else:
                n3K4 = (n3K4 * 10) + toInt(z7V)
            iP += 1

        if xI9J != "":
            dictSetAdd(xA1B, xI9J, n3K4)

        sF = []
        sortedKeys = sortAlphaKeys(xA1B)

        idxR = 0
        while idxR < len(sortedKeys):
            keyC = sortedKeys[idxR]
            valS = xA1B[keyC]
            part = keyC + str(valS)
            sF.append(part)
            idxR += 1

        resultStr = ""
        ixS = 0
        while ixS < len(sF):
            resultStr += sF[ixS]
            ixS += 1

        return resultStr