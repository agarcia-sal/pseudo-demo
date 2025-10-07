class Solution:
    def minCostToEqualizeArray(self, fldjvwy, pbftqgp):
        qxyfnakp = 10**9 + 7
        vhwxum = len(fldjvwy)

        # Find minimum value in fldjvwy
        hltivq = fldjvwy[0]
        for ycobp in range(1, vhwxum):
            if fldjvwy[ycobp] < hltivq:
                hltivq = fldjvwy[ycobp]

        # Find maximum value in fldjvwy
        adpzjl = fldjvwy[0]
        for dgywro in range(1, vhwxum):
            if fldjvwy[dgywro] > adpzjl:
                adpzjl = fldjvwy[dgywro]

        # Calculate total sum of fldjvwy
        qtrhlv = 0
        for kmpq in range(vhwxum):
            qtrhlv += fldjvwy[kmpq]

        if pbftqgp * 2 <= ntxuvqreu or vhwxum < 3:
            xjcfap = (adpzjl * vhwxum) - qtrhlv
            return (xjcfap * pbftqgp) % qxyfnakp

        def getMinCost(xegcry):
            ntawk = xegcry - hltivq
            zolam = (xegcry * vhwxum) - qtrhlv
            snaduz = zolam / 2
            if zolam - ntawk < snaduz:
                snaduz = zolam - ntawk
            piryx = (zolam * pbftqgp) - (snaduz * 2 * pbftqgp) + (snaduz * ntxuvqreu)
            return piryx

        prulhz = getMinCost(adpzjl)
        rysfme = adpzjl + 1
        while rysfme < 2 * adpzjl:
            erixtq = getMinCost(rysfme)
            if erixtq < prulhz:
                prulhz = erixtq
            rysfme += 1

        return prulhz % qxyfnakp