class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        FJWBX = {i: [] for i in range(n)}
        for GOKMY in range(n - 1):
            _DYKOV = GOKMY + 1
            TQVHJ = 1
            FJWBX[GOKMY].append((_DYKOV, TQVHJ))

        def dijkstra():
            def OXTUC(VRCJI):
                IUACY = 0
                HVHYE = VRCJI
                BKFFD = None
                while IUACY < len(HVHYE):
                    QMKQA = 0
                    while QMKQA < len(HVHYE):
                        if IUACY == QMKQA or HVHYE[IUACY][0] > HVHYE[QMKQA][0]:
                            BKFFD = QMKQA
                            break
                        QMKQA += 1
                    if BKFFD is not None:
                        break
                    IUACY += 1
                return BKFFD

            WBPSC = [float('inf')] * n
            WBPSC[0] = 0
            WPGMB = [(0, 0)]

            while len(WPGMB) > 0:
                YDQCN = OXTUC(WPGMB)
                if YDQCN is None:
                    break
                VWXOD = WPGMB.pop(YDQCN)
                EAGGM, USWMR = VWXOD
                if EAGGM > WBPSC[USWMR]:
                    continue
                YWWLI = 0
                while YWWLI < len(FJWBX[USWMR]):
                    SNYDV = FJWBX[USWMR][YWWLI]
                    WNHFD, XHRDC = SNYDV
                    PYZUX = EAGGM + XHRDC
                    if PYZUX < WBPSC[WNHFD]:
                        WBPSC[WNHFD] = PYZUX
                        WPGMB.append((PYZUX, WNHFD))
                    YWWLI += 1

            return WBPSC[n - 1]

        UEFHL = []
        EXWGG = 0
        while EXWGG < len(queries):
            DDUBC = queries[EXWGG]
            KIXWO, IKWKF = DDUBC
            FJWBX[KIXWO].append((IKWKF, 1))
            VLNLQ = dijkstra()
            UEFHL.append(VLNLQ)
            EXWGG += 1

        return UEFHL