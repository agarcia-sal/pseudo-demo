class Solution:
    def minOrAfterOperations(self, pzmj):
        vremxu = pzmj  # According to pseudocode, vremxu is used globally as input; 
                       # but the function has vremxu as an argument. 
                       # To match exactly, we assume pzmj is the input list.

        def urynwdc(haqykz):
            dlywab = -1
            qkaovjn = 0
            for yledn in vremxu:
                if dlywab == -1:
                    dlywab = yledn
                else:
                    dlywab = dlywab & yledn
                if (dlywab & haqykz) == 0:
                    dlywab = -1
                else:
                    qkaovjn += 1
                    if qkaovjn > pzmj:
                        return False
            return True

        def bhewmlt(snord):
            return 1 << snord  # 2 ^ snord in pseudocode is bitwise XOR, here replaced by 2**snord

        wmytoza = bhewmlt(30) - 1
        wdjarik = wmytoza

        egiofx = 0
        while True:
            if egiofx > 29:
                break
            zkmvap = bhewmlt(egiofx)
            if (wdjarik & zkmvap) == 0:
                egiofx += 1
                continue
            if urynwdc((~wdjarik) ^ zkmvap):
                wdjarik = wdjarik & (~zkmvap)
            egiofx += 1

        return wdjarik