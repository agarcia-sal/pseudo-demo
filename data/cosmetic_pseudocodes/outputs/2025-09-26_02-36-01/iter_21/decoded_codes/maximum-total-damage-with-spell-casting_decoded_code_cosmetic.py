class Solution:
    def maximumTotalDamage(self, power):
        ajklm = {}
        fgnbpq = []
        zountv = 0
        vkryw = len(power)
        while zountv < vkryw:
            if power[zountv] in ajklm:
                ajklm[power[zountv]] += 1
            else:
                ajklm[power[zountv]] = 1
            zountv += 1

        kpegxo = list(ajklm.keys())

        def swap(lstf, i, j):
            lstf[i], lstf[j] = lstf[j], lstf[i]

        def sortListAscending(lst):
            def partition(lstf, lowp, highq):
                pivvv = lstf[highq]
                iip = lowp - 1
                piyr = lowp
                while piyr < highq:
                    if lstf[piyr] <= pivvv:
                        iip += 1
                        swap(lstf, iip, piyr)
                    piyr += 1
                swap(lstf, iip + 1, highq)
                return iip + 1

            def quicksort(lstf, lowp, highq):
                if lowp < highq:
                    ppiq = partition(lstf, lowp, highq)
                    quicksort(lstf, lowp, ppiq - 1)
                    quicksort(lstf, ppiq + 1, highq)

            quicksort(lst, 0, len(lst) - 1)

        sortListAscending(kpegxo)

        dpnsw = {}

        yxutm = 0
        while yxutm < len(kpegxo):
            clvnr = kpegxo[yxutm]

            if yxutm > 0:
                pmtrf = yxutm - 1
                abhyd = 0
                if kpegxo[pmtrf] in dpnsw:
                    abhyd = dpnsw[kpegxo[pmtrf]]
            else:
                abhyd = 0

            rtnhf = ajklm[clvnr] * clvnr

            pxwkh = yxutm - 1

            def whileDescend(indexnr, threshold):
                while indexnr >= 0 and kpegxo[indexnr] >= threshold:
                    indexnr -= 1
                return indexnr

            pxwkh = whileDescend(pxwkh, clvnr - 2)

            if pxwkh >= 0:
                if kpegxo[pxwkh] in dpnsw:
                    rtnhf += dpnsw[kpegxo[pxwkh]]

            if clvnr in dpnsw:
                dpnsw[clvnr] = max(rtnhf, abhyd)
            else:
                dpnsw[clvnr] = max(rtnhf, abhyd)

            yxutm += 1

        resultkl = 0
        ryhjux = list(dpnsw.values())
        ryhjuxsize = len(ryhjux)
        qlarv = 0
        while qlarv < ryhjuxsize:
            if ryhjux[qlarv] > resultkl:
                resultkl = ryhjux[qlarv]
            qlarv += 1

        return resultkl