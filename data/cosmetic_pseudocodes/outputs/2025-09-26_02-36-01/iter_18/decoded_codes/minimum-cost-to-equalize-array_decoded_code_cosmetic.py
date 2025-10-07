class Solution:
    def minCostToEqualizeArray(self, vwzxadv, oqwmkxfd, jdebwah):
        ONE_BILLION_SEVEN = 1000000007
        syhvbz = len(vwzxadv)
        pquilm = min(vwzxadv)
        krqfnj = max(vwzxadv)
        dzjxls = 0

        idx_f = 0
        while idx_f < syhvbz:
            dzjxls += vwzxadv[idx_f]
            idx_f += 1

        if (oqwmkxfd * 2) <= jdebwah or syhvbz < 3:
            zsemto = (krqfnj * syhvbz) - dzjxls
            return (oqwmkxfd * zsemto) % ONE_BILLION_SEVEN

        def qyxdpv(tzphmx):
            xnebrk = tzphmx - pquilm
            fidtln = (tzphmx * syhvbz) - dzjxls
            ragtbo = min(fidtln // 2, fidtln - xnebrk)
            return (oqwmkxfd * fidtln) - (2 * ragtbo * oqwmkxfd) + (jdebwah * ragtbo)

        ytgplz = None
        wfanqx = krqfnj
        qakvru = (2 * krqfnj) - 1

        while wfanqx <= qakvru:
            gthcjy = qyxdpv(wfanqx)
            if ytgplz is None or gthcjy < ytgplz:
                ytgplz = gthcjy
            wfanqx += 1

        return ytgplz % ONE_BILLION_SEVEN