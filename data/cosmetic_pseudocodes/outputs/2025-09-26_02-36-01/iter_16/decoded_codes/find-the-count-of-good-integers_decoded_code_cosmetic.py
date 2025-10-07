class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        auroxcwqgh = []
        opmlrgzvn = 0
        bpeaokytz = set()
        wqztcedi = 10 ** ((n - 1) // 2)

        mcuopkhzn = 0
        while mcuopkhzn < n + 1:
            hztfnapx = 1
            vdfoueqj = 2
            kxsozwav = 1
            while vdfoueqj <= mcuopkhzn:
                hztfnapx *= kxsozwav
                vdfoueqj += 1
                kxsozwav += 1
            auroxcwqgh.append(hztfnapx)
            mcuopkhzn += 1

        # The pseudocode has a while loop resetting opmlrgzvn to 0 while it's negative,
        # then opmlrgzvn is set to 0. Since opmlrgzvn is already 0, we simply keep it 0.
        opmlrgzvn = 0

        dwpskhfcry = wqztcedi
        upper_limit = wqztcedi * 10
        while dwpskhfcry <= upper_limit - 1:
            ypkrtnezf = str(dwpskhfcry)
            mfvgxolrb = n % 2
            revypktzd = ypkrtnezf[::-1]
            tqjwdcof = ypkrtnezf + revypktzd[mfvgxolrb:]

            if int(tqjwdcof) % k != 0:
                dwpskhfcry += 1
                continue

            tjiydpmwz = list(tqjwdcof)
            tjiydpmwz.sort()
            yndcarpmg = ''.join(tjiydpmwz)

            if yndcarpmg in bpeaokytz:
                dwpskhfcry += 1
                continue

            bpeaokytz.add(yndcarpmg)

            rqbiavztp = {}
            for ch in yndcarpmg:
                rqbiavztp[ch] = rqbiavztp.get(ch, 0) + 1

            if '0' in rqbiavztp and rqbiavztp['0'] > 0:
                lnazgwfys = n - rqbiavztp['0']
                pasefqdbv = auroxcwqgh[n - 1]
                res = lnazgwfys * pasefqdbv
            else:
                res = auroxcwqgh[n]

            cenyplxdr = list(rqbiavztp.values())
            for val in cenyplxdr:
                res //= auroxcwqgh[val]

            opmlrgzvn += res
            dwpskhfcry += 1

        return opmlrgzvn