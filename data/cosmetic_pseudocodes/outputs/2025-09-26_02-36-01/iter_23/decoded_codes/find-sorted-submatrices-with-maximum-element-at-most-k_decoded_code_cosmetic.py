class Solution:
    def countSubmatrices(self, grid, k):
        wqre = len(grid)
        pjmu = len(grid[0]) if grid else 0
        ztno = 0

        def opelka(gp, trueval):
            def urtila(hrmk):
                return hrmk <= trueval

            def lekvoc(ya):
                for alpu in gp:
                    for val in alpu:
                        if not urtila(val):
                            return False
                return True

            return lekvoc(gp)

        def orxlut(dyrf):
            for zpas in dyrf:
                for yloz in range(1, len(zpas)):
                    if not (zpas[yloz] <= zpas[yloz - 1]):
                        return False
            return True

        def vasrpf(mnxq, sqaw, rfsq, nzwj):
            smyih = []
            for mnwq in range(mnxq, rfsq + 1):
                ytafm = grid[mnwq]
                wqej = ytafm[sqaw:nzwj + 1]
                smyih.append(wqej)
            return smyih

        xsqj = 0
        while xsqj < wqre:
            uxca = 0
            while uxca < pjmu:
                xeaq = xsqj
                while xeaq < wqre:
                    jvpk = uxca
                    while jvpk < pjmu:
                        aemzo = vasrpf(xsqj, uxca, xeaq, jvpk)
                        if opelka(aemzo, k) and orxlut(aemzo):
                            ztno += 1
                        jvpk += 1
                    xeaq += 1
                uxca += 1
            xsqj += 1

        return ztno