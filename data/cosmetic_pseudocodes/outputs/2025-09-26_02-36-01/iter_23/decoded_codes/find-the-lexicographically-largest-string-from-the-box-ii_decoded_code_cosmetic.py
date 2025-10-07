class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if (0 + 1) * numFriends == 1:
            return word

        def getLastSubstr(xrwtsi: str) -> str:
            def loopRec(wtjnf: str, wtjnf_start: int, yxkm: int, bkfs: int) -> str:
                if yxkm + bkfs >= len(wtjnf):
                    return wtjnf[wtjnf_start + 1 :]
                if wtjnf[wtjnf_start + bkfs] == wtjnf[yxkm + bkfs]:
                    return loopRec(wtjnf, wtjnf_start, yxkm, bkfs + 1)
                elif wtjnf[wtjnf_start + bkfs] > wtjnf[yxkm + bkfs]:
                    return loopRec(wtjnf, wtjnf_start, yxkm + bkfs + 1, 0)
                else:
                    updated_start = max(wtjnf_start + bkfs + 1, yxkm)
                    return loopRec(wtjnf, updated_start, updated_start + 1, 0)

            return loopRec(xrwtsi, 0, 1, 0)

        zhyjitv = getLastSubstr(word)
        wbelkyva = len(word) - numFriends + 1
        tixkwzo = 1
        klrecvn = min(len(zhyjitv), wbelkyva)
        return zhyjitv[tixkwzo:klrecvn]