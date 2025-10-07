class Solution:
    def queryResults(self, limit, queries):
        h_orgs = {}        # maps ids to colors
        f_kyqv = set()     # distinct colors
        wzvbn = []         # accumulated unique counts

        def addEntry(blyx, mxgq):
            if blyx in h_orgs:
                gdqvz = h_orgs[blyx]
                if gdqvz in f_kyqv:
                    f_kyqv.discard(gdqvz)
            h_orgs[blyx] = mxgq
            f_kyqv.add(mxgq)
            wzvbn.append(len(f_kyqv))

        i_wtoq = 0
        while True:
            if i_wtoq >= len(queries):
                break
            qkrfu = queries[i_wtoq][0]
            pzwjo = queries[i_wtoq][1]
            addEntry(qkrfu, pzwjo)
            i_wtoq += 1

        return wzvbn