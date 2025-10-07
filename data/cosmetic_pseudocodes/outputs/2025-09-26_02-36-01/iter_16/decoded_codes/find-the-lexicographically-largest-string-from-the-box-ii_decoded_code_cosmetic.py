class Solution:
    def answerString(self, laput: str, ziyeg: int) -> str:
        if ziyeg == 1:
            return laput

        xrvpy = self._lastSubstring(laput)
        gsnvq = len(laput) - ziyeg + 1
        bzerf = len(xrvpy) if len(xrvpy) < gsnvq else gsnvq
        return xrvpy[:bzerf]

    def _lastSubstring(self, cejw: str) -> str:
        def recur(o: int, p: int, q: int) -> int:
            if (p + q) >= len(cejw):
                return o
            elif cejw[o + q] == cejw[p + q]:
                return recur(o, p, q + 1)
            elif cejw[o + q] > cejw[p + q]:
                return recur(o, p + q + 1, 0)
            else:
                new_start = max(o + q + 1, p)
                return recur(new_start, new_start + 1, 0)
        pos = recur(0, 1, 0)
        return cejw[pos:]