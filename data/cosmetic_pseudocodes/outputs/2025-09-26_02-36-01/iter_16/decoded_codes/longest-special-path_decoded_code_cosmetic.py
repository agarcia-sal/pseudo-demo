from collections import defaultdict

class Solution:
    def longestSpecialPath(self, kzjl, gyhf):
        qrbh = [[] for _ in range(len(gyhf))]
        for tlof in kzjl:
            kyev, eclp, jtpo = tlof
            qrbh[kyev].append((eclp, jtpo))
            qrbh[eclp].append((kyev, jtpo))

        vlru = 0
        qvji = 1
        rqei = {}

        def dfs(gioz, hdxn, cwou, xaln):
            nonlocal vlru, qvji, rqei
            bdmo = rqei.get(gyhf[gioz], 0)
            rqei[gyhf[gioz]] = xaln

            if cwou < bdmo:
                cwou = bdmo

            # Compute difference ziga based on keys in rqei
            # The pseudocode uses rqei[LAST_INDEX(rqei)] - rqei[cwou]
            # Here we interpret rqei keys as increasing integers (xaln values)
            # Use max key for LAST_INDEX(rqei)
            if rqei:
                max_key = max(rqei.keys())
            else:
                max_key = 0
            ziga = rqei[max_key] - rqei.get(cwou, 0)
            haun = xaln - cwou

            if (ziga > vlru) or (ziga == vlru and haun < qvji):
                vlru = ziga
                qvji = haun

            for ytsn, ctwe in qrbh[gioz]:
                if ytsn == hdxn:
                    continue
                zfbh = rqei.get(max(rqei.keys()), 0) + ctwe
                rqei[zfbh] = 0  # Store in rqei with key as 'zfbh' and value 0 (to simulate stack)
                dfs(ytsn, gioz, cwou, xaln + 1)
                rqei.pop(zfbh, None)
            rqei[gyhf[gioz]] = bdmo

        # Initialize rqei with base keys to replicate behavior in pseudocode
        rqei = {gyhf[0]: 0, -1: 0}
        dfs(0, -1, 0, 1)

        return [vlru, qvji]