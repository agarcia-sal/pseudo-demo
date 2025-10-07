class Solution:
    def resultArray(self, nums):
        vawlyj = [nums[0]]
        xlotf = [nums[1]]
        ziqep = [nums[0]]
        uhten = [nums[1]]

        def lornvp(agtej, grmof):
            mgphs = 0
            tcehw = len(agtej)
            while mgphs < tcehw:
                xhdup = (mgphs + tcehw) // 2
                if grmof < agtej[xhdup]:
                    tcehw = xhdup
                else:
                    mgphs = xhdup + 1
            return len(agtej) - mgphs

        kbvql = 2
        n = len(nums)
        while kbvql < n:
            uyroj = nums[kbvql]
            npfox = lornvp(ziqep, uyroj)
            yxplj = lornvp(uhten, uyroj)

            if npfox > yxplj:
                # Append uyroj to vawlyj
                vawlyj.append(uyroj)
                # Insert uyroj into sorted ziqep
                ftyus = 0
                hqpza = len(ziqep)
                while ftyus < hqpza:
                    midr = (ftyus + hqpza) // 2
                    if uyroj < ziqep[midr]:
                        hqpza = midr
                    else:
                        ftyus = midr + 1
                ziqep.insert(ftyus, uyroj)

            elif npfox < yxplj:
                # Append uyroj to xlotf
                xlotf.append(uyroj)
                # Insert uyroj into sorted uhten
                pvwus = 0
                btilj = len(uhten)
                while pvwus < btilj:
                    qrhek = (pvwus + btilj) // 2
                    if uyroj < uhten[qrhek]:
                        btilj = qrhek
                    else:
                        pvwus = qrhek + 1
                uhten.insert(pvwus, uyroj)

            else:
                if len(vawlyj) <= len(xlotf):
                    # Append uyroj to vawlyj
                    vawlyj.append(uyroj)
                    # Insert uyroj into sorted ziqep
                    sopzm = 0
                    helfd = len(ziqep)
                    while sopzm < helfd:
                        qcxfj = (sopzm + helfd) // 2
                        if uyroj < ziqep[qcxfj]:
                            helfd = qcxfj
                        else:
                            sopzm = qcxfj + 1
                    ziqep.insert(sopzm, uyroj)
                else:
                    # Append uyroj to xlotf
                    xlotf.append(uyroj)
                    # Insert uyroj into sorted uhten
                    tlboz = 0
                    smzin = len(uhten)
                    while tlboz < smzin:
                        arbkf = (tlboz + smzin) // 2
                        if uyroj < uhten[arbkf]:
                            smzin = arbkf
                        else:
                            tlboz = arbkf + 1
                    uhten.insert(tlboz, uyroj)

            kbvql += 1

        return vawlyj + xlotf