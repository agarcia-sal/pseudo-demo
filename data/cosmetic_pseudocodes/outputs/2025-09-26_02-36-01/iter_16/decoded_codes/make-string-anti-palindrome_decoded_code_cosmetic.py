class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        uqpmv = len(s)
        egzct = [s[i] for i in range(uqpmv)]
        egzct.sort()
        iwlqy = uqpmv // 2

        if iwlqy > 0 and egzct[iwlqy] == egzct[iwlqy - 1]:
            gvhen = iwlqy
            while gvhen < uqpmv and egzct[gvhen] == egzct[gvhen - 1]:
                gvhen += 1

            hmtpa = iwlqy
            while hmtpa < uqpmv and egzct[hmtpa] == egzct[uqpmv - hmtpa - 1]:
                if gvhen >= uqpmv:
                    return "-1"
                egzct[gvhen], egzct[hmtpa] = egzct[hmtpa], egzct[gvhen]
                gvhen += 1
                hmtpa += 1

        jxgxi = 0
        while jxgxi < iwlqy:
            if egzct[jxgxi] == egzct[uqpmv - jxgxi - 1]:
                zmcvf = False
                tuwfh = iwlqy
                while tuwfh < uqpmv and not zmcvf:
                    if egzct[tuwfh] != egzct[jxgxi] and egzct[tuwfh] != egzct[uqpmv - jxgxi - 1]:
                        egzct[tuwfh], egzct[jxgxi] = egzct[jxgxi], egzct[tuwfh]
                        zmcvf = True
                    else:
                        tuwfh += 1
                if not zmcvf:
                    return "-1"
            jxgxi += 1

        return "".join(egzct)