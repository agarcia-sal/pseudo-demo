class Solution:
    MOD = 10**9 + 7

    def sumOfPower(self, qsdap, lfen):
        def modAdd(pnvw, rjch):
            return (pnvw + rjch) - self.MOD * ((pnvw + rjch) // self.MOD)

        def powerOfTwo(ixa):
            res = 1
            idx = 0
            while idx < ixa:
                res = modAdd(res, res)
                idx += 1
            return res

        xdpf = len(qsdap)
        xtzm = [[0] * (lfen + 1) for _ in range(xdpf + 1)]
        xtzm[0][0] = 1

        vxrp = 1
        while vxrp <= xdpf:
            lmisc = 0
            while lmisc <= lfen:
                xtzm[vxrp][lmisc] = xtzm[vxrp - 1][lmisc]
                if lmisc >= qsdap[vxrp - 1]:
                    xtzm[vxrp][lmisc] = modAdd(xtzm[vxrp][lmisc], xtzm[vxrp - 1][lmisc - qsdap[vxrp - 1]])
                lmisc += 1
            vxrp += 1

        dpowyo = 0
        zizry = powerOfTwo(xdpf)
        bzfr = 1
        while bzfr < zizry:
            eajvg = 0
            gbxen = 0
            wyso = bzfr
            while wyso > 0:
                if wyso % 2 == 1:
                    eajvg += qsdap[gbxen]
                gbxen += 1
                wyso //= 2
            if eajvg == lfen:
                dpowyo = (dpowyo + powerOfTwo(xdpf - gbxen)) % self.MOD
            bzfr += 1

        return dpowyo