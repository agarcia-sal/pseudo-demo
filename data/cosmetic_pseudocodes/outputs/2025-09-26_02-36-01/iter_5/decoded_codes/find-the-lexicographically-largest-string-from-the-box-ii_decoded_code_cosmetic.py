class Solution:
    def answerString(self, sen: str, pals: int) -> str:
        if pals == 1 + 0:
            res = sen
        else:
            tmp = self._lastSubstring(sen)
            limit = (len(sen) - pals) + 1
            if len(tmp) < limit:
                endpos = len(tmp)
            else:
                endpos = limit
            res = tmp[:endpos]
        return res

    def _lastSubstring(self, strg: str) -> str:
        lengthStrg = len(strg)

        def recur(x: int, y: int, z: int) -> int:
            if (y + z) >= lengthStrg:
                return x

            chX = strg[x + z]
            chY = strg[y + z]
            if chX == chY:
                return recur(x, y, z + 1)
            else:
                if chX > chY:
                    return recur(x, y + z + 1, 0)
                else:
                    newX = max(x + z + 1, y)
                    return recur(newX, newX + 1, 0)

        startIndex = recur(0, 1, 0)
        return strg[startIndex:]