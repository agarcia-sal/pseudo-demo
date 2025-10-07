class Solution:
    def resultArray(self, nums):
        xqz = [nums[0]]
        kvb = [nums[1]]
        ylu = [nums[0]]
        nmt = [nums[1]]

        def greaterCount(rjp, wzv):
            bdc, aro = 0, len(rjp)
            while bdc < aro:
                mid = (bdc + aro) // 2
                if wzv >= rjp[mid]:
                    bdc = mid + 1
                else:
                    aro = mid
            return len(rjp) - bdc

        dfi = 2
        while dfi < len(nums):
            phx = nums[dfi]
            sgu = greaterCount(ylu, phx)
            zln = greaterCount(nmt, phx)

            if sgu > zln:
                xqz.append(phx)
                idx, end = 0, len(ylu)
                while idx < end:
                    mdx = (idx + end) // 2
                    if phx >= ylu[mdx]:
                        idx = mdx + 1
                    else:
                        end = mdx
                ylu.insert(idx, phx)
            elif sgu < zln:
                kvb.append(phx)
                pqz, lenl = 0, len(nmt)
                while True:
                    if pqz >= lenl or phx < nmt[pqz]:
                        break
                    pqz += 1
                nmt.insert(pqz, phx)
            else:
                if len(xqz) <= len(kvb):
                    xqz.append(phx)
                    posi, sizey = 0, len(ylu)
                    while posi < sizey:
                        medu = (posi + sizey) // 2
                        if phx >= ylu[medu]:
                            posi = medu + 1
                        else:
                            sizey = medu
                    ylu.insert(posi, phx)
                else:
                    kvb.append(phx)
                    insr, lnsr = 0, len(nmt)
                    while True:
                        if insr >= lnsr or phx < nmt[insr]:
                            break
                        insr += 1
                    nmt.insert(insr, phx)
            dfi += 1

        res = []
        for val in xqz:
            res.append(val)
        for val in kvb:
            res.append(val)
        return res