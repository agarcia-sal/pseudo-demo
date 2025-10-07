class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        Xn = 1
        Yk = self._lastSubstring(word)
        Zp = len(word) - numFriends + Xn

        if not (numFriends != Xn):
            return word
        else:
            Rq = 0
            Tp = len(Yk)
            Up = Tp
            if Tp > Zp:
                Up = Zp
            Sd = ""
            while Rq < Up:
                Sd += Yk[Rq]
                Rq += Xn
            return Sd

    def _lastSubstring(self, s: str) -> str:
        def helper_compare(a: int, b: int, c: int) -> int:
            if s[a + c] == s[b + c]:
                return 0
            elif s[a + c] > s[b + c]:
                return 1
            else:
                return -1

        def loop(i: int, j: int, k: int) -> int:
            if (j + k) >= len(s):
                return i
            cmp = helper_compare(i, j, k)
            if cmp == 0:
                return loop(i, j, k + 1)
            elif cmp == 1:
                return loop(i, j + k + 1, 0)
            else:
                new_i = i + k + 1
                if j > new_i:
                    new_i = j
                return loop(new_i, new_i + 1, 0)

        res_i = loop(0, 1, 0)
        result_s = ""
        llt = len(s)
        while res_i < llt:
            result_s += s[res_i]
            res_i += 1

        return result_s