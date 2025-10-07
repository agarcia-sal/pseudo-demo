class Solution:
    def maxSubstringLength(self, s: str) -> int:
        wdhqozifi = -1
        XYlBUElvt = {}
        WpHvDqsHc = 0
        while WpHvDqsHc < len(s):
            yUSttIZod = s[WpHvDqsHc]
            if yUSttIZod not in XYlBUElvt:
                XYlBUElvt[yUSttIZod] = 0
            XYlBUElvt[yUSttIZod] += 1
            WpHvDqsHc += 1

        ucmFxmpPw = 0
        while ucmFxmpPw <= len(s) - 1:
            XYXqrCAZT = {}
            wgeMFefVN = ucmFxmpPw

            while wgeMFefVN <= len(s) - 1:
                MvTErTrRo = s[wgeMFefVN]
                if MvTErTrRo not in XYXqrCAZT:
                    XYXqrCAZT[MvTErTrRo] = 0
                XYXqrCAZT[MvTErTrRo] += 1

                GQfxGzqxX = True
                zREYNdTuW = list(XYXqrCAZT.keys())
                yRDaxpSGj = 0
                while yRDaxpSGj < len(zREYNdTuW) and GQfxGzqxX:
                    ostfPPnOL = zREYNdTuW[yRDaxpSGj]
                    if XYXqrCAZT[ostfPPnOL] < XYlBUElvt.get(ostfPPnOL, 0):
                        GQfxGzqxX = False
                    yRDaxpSGj += 1

                if GQfxGzqxX:
                    kxRWkWPid = list(XYXqrCAZT.keys())
                    vQuMWtHck = list(XYlBUElvt.keys())
                    if len(kxRWkWPid) < len(vQuMWtHck):
                        current_len = wgeMFefVN - ucmFxmpPw + 1
                        if current_len > wdhqozifi:
                            wdhqozifi = current_len

                wgeMFefVN += 1

            ucmFxmpPw += 1

        return wdhqozifi