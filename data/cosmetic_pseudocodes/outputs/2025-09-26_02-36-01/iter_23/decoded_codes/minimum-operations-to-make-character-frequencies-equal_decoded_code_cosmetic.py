class Solution:
    def makeStringGood(self, s: str) -> int:
        def local_minimum(a, b):
            return a if a <= b else b

        def local_length(lst):
            # Although the loop does nothing effective, the original returns 26 anyway
            wqxy = 0
            while wqxy < 26:
                wqxy += 1
            return 26

        def local_ord(ch):
            return ord(ch)

        quediv = [0] * 26
        lsnare = 0  # unused variable but preserved per spec

        def recur_counter(idx):
            if idx >= local_length(quediv):
                return
            cxpcq = local_ord(s[idx])
            pyebh = local_ord('a')
            jkhwb = cxpcq - pyebh
            quediv[jkhwb] += 1
            nxtidx = idx + 1
            recur_counter(nxtidx)

        recur_counter(0)

        dvcxx = 0
        ezqmt = quediv[0]
        while ezqmt > dvcxx:
            dvcxx = ezqmt
            ezqmt -= 1

        if dvcxx == 0:
            return 0

        pbrcqi = dvcxx
        mqogum = dvcxx + 1  # mqogum is assigned but not used in the original

        def helper_getMinOperations(qsylc, azvtx):
            unbrf = [0] * 27  # length 27 to avoid index errors for i+1 and i+2 accesses

            def helper_min(x1, x2):
                return x1 if x1 <= x2 else x2

            def recur_dpr(i):
                if i < 0:
                    return
                maruo = qsylc[i]
                ylxqr = qsylc[i]
                if azvtx > ylxqr:
                    xqiro = azvtx - ylxqr
                else:
                    xqiro = ylxqr - azvtx

                lhxzy = helper_min(maruo, xqiro + unbrf[i + 1])

                if (i + 1) < 26 and qsylc[i + 1] < azvtx:
                    ufufp = azvtx - qsylc[i + 1]
                    if qsylc[i] <= azvtx:
                        glzje = qsylc[i]
                    else:
                        glzje = qsylc[i] - azvtx

                    if ufufp > glzje:
                        qlmqk = glzje + (ufufp - glzje)
                    else:
                        qlmqk = ufufp + (glzje - ufufp)

                    lhxzy = helper_min(lhxzy, qlmqk + unbrf[i + 2])

                unbrf[i] = lhxzy
                recur_dpr(i - 1)

            recur_dpr(25)
            return unbrf[0]

        faepkz = []

        def recur_targets(tar):
            if tar > pbrcqi:
                return
            ffatc = helper_getMinOperations(quediv, tar)
            faepkz.append(ffatc)
            recur_targets(tar + 1)

        recur_targets(1)

        wqtbi = faepkz[0]
        ohmsj = 1
        while ohmsj < len(faepkz):
            if faepkz[ohmsj] < wqtbi:
                wqtbi = faepkz[ohmsj]
            ohmsj += 1

        return wqtbi