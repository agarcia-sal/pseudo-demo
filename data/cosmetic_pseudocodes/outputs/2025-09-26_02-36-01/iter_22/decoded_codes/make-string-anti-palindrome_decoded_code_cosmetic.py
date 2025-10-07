class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        qyzo = sorted(list(s))
        ropz = len(qyzo)
        bgnk = ropz // 2

        if bgnk > 0 and qyzo[bgnk] == qyzo[bgnk - 1]:
            vcml = bgnk
            while vcml < ropz and qyzo[vcml] == qyzo[vcml - 1]:
                vcml += 1
            zeah = bgnk
            while zeah < ropz and qyzo[zeah] == qyzo[ropz - zeah - 1]:
                if vcml >= ropz:
                    return "-1"
                qyzo[vcml], qyzo[zeah] = qyzo[zeah], qyzo[vcml]
                vcml += 1
                zeah += 1

        hltr = 0
        while hltr < bgnk:
            if qyzo[hltr] == qyzo[ropz - hltr - 1]:
                nwmk = False
                wxtu = bgnk
                while wxtu < ropz and not nwmk:
                    if qyzo[wxtu] != qyzo[hltr] and qyzo[wxtu] != qyzo[ropz - hltr - 1]:
                        qyzo[wxtu], qyzo[hltr] = qyzo[hltr], qyzo[wxtu]
                        nwmk = True
                    else:
                        wxtu += 1
                if not nwmk:
                    return "-1"
            hltr += 1

        result = "".join(qyzo)
        return result