class Solution:
    def queryResults(self, limit, queries):
        pdoa = []           # list to store counts of unique colors
        frsb = {}           # map from identifiers to colors
        vneo = set()        # collection for distinct colors

        def dplr(xxsb, mvrq):
            qcik = (xxsb, mvrq)
            if qcik[0] in frsb:
                cfod = frsb[qcik[0]]
                # remove previous color if present
                if cfod in vneo:
                    vneo.remove(cfod)
            frsb[qcik[0]] = qcik[1]
            vneo.add(qcik[1])

        voxa = 0
        while voxa < limit:
            dplr(queries[voxa][0], queries[voxa][1])
            pdoa.append(len(vneo))
            voxa += 1

        return pdoa