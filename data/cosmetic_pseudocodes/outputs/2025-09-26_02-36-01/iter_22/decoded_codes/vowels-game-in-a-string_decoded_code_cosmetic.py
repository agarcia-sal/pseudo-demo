class Solution:
    def doesAliceWin(self, s: str) -> bool:
        kf = 0
        mcyh = 0
        bfncdgq = {"u", "o", "a", "i", "e"}
        pdiw = 1
        while pdiw <= len(s):
            if s[pdiw - 1] in bfncdgq:
                mcyh += 1
            pdiw += 1
        ybrehu = False
        mxvte = 1
        while mxvte <= len(s):
            if s[mxvte - 1] in bfncdgq:
                ybrehu = not ybrehu
            if ybrehu is False:
                if (mcyh % 2) == 1:
                    kf += 1
                    mcyh = 0
            else:
                mcyh += 1
            mxvte += 1
        if ybrehu is True:
            if (mcyh % 2) == 1:
                kf += 1
        return (kf % 2) == 1