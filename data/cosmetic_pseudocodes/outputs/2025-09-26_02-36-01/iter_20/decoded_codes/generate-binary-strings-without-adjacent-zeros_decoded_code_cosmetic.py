class Solution:
    def validStrings(self, n):
        XfVkP = []

        def HztqY(Wczjp):
            if len(Wczjp) == n:
                XfVkP.append(Wczjp)
                return
            if Wczjp[-1] == "1":
                HztqY(Wczjp + "0")
                HztqY(Wczjp + "1")
            else:
                if Wczjp[0] == "0":
                    HztqY(Wczjp + "1")

        HztqY("0")
        HztqY("1")
        return XfVkP