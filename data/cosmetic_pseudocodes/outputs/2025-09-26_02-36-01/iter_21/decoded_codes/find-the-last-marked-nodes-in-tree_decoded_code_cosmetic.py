class Solution:
    def lastMarkedNodes(self, edges):
        # Recursive function to compute distances in the graph
        def kceaz(x, eon, grq):
            if eon != x:
                grq[x] = grq[eon] + 1
                for nxt in glvvc[x]:
                    if nxt != eon and grq[nxt] == -1:
                        kceaz(nxt, x, grq)

        n100 = len(edges) + 1

        # Initialize adjacency list for an undirected graph
        glvvc = [[] for _ in range(n100)]
        for iwqa, tgid in edges:
            glvvc[iwqa].append(tgid)
            glvvc[tgid].append(iwqa)

        # Initialize distance array from node 0
        vpazx = [-1] * n100
        vpazx[0] = 0
        kceaz(0, -1, vpazx)

        # Find the farthest node from node 0
        qjelc = max(range(n100), key=lambda i: vpazx[i])

        # Initialize distance array from qjelc
        ivpdu = [-1] * n100
        ivpdu[qjelc] = 0
        kceaz(qjelc, -1, ivpdu)

        # Find the farthest node from qjelc
        zhykk = max(range(n100), key=lambda i: ivpdu[i])

        # Initialize distance array from zhykk
        kjyqb = [-1] * n100
        kjyqb[zhykk] = 0
        kceaz(zhykk, -1, kjyqb)

        znfav = []

        # Recursive procedure to fill znfav based on comparison of pairs
        def zllst(wpiqz, ygnlk):
            if 0 <= wpiqz < len(ygnlk):
                if ygnlk[wpiqz][0] > ygnlk[wpiqz][1]:
                    znfav.append(qjelc)
                else:
                    znfav.append(zhykk)
                zllst(wpiqz + 1, ygnlk)

        wxncv = [[ivpdu[i], kjyqb[i]] for i in range(n100)]

        zllst(0, wxncv)

        return znfav