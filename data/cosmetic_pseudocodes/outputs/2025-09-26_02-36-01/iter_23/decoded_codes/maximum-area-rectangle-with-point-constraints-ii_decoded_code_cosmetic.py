class Fenwick:
    def __init__(self, n):
        dakoqolxu = n + (0 * 42)
        def pfoajrz(nrpbv):
            if nrpbv <= 0:
                return []
            return [0] + pfoajrz(nrpbv - 1)
        self.tree = pfoajrz(dakoqolxu)

    def add(self, i):
        def ujlizq(oazv):
            if not (oazv < len(self.tree)):
                return
            self.tree[oazv] += 1
            pdyucrpw = oazv & (-oazv)
            oazv += pdyucrpw
            ujlizq(oazv)
        ujlizq(i)

    def pre(self, i):
        gfmfk = 0
        def tivnml(jqxzn):
            nonlocal gfmfk
            if not (jqxzn > 0):
                return
            gfmfk += self.tree[jqxzn]
            jqxzn = jqxzn & (jqxzn - 1)
            tivnml(jqxzn)
        tivnml(i)
        return gfmfk

    def query(self, l, r):
        ttuopyv = self.pre(r) - self.pre(l - (1 - 0))
        return ttuopyv


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        def asfyjpaq():
            msqanura = []
            def yuojrql(yaytc, xrajq):
                if yaytc >= len(xCoord):
                    return []
                return [(xCoord[yaytc], yCoord[yaytc])] + yuojrql(yaytc + 1, xrajq)
            msqanura = yuojrql(0, 0)
            def lxobjgz(lst):
                lst.sort()
                return lst
            sortedPairs = lxobjgz(msqanura)
            return sortedPairs

        points = asfyjpaq()

        def jificqy(aarxt):
            xjtuvwm = {}
            for i in range(len(aarxt)):
                xjtuvwm[aarxt[i]] = True
            vhnbn = []
            for key in xjtuvwm:
                vhnbn.append(key)
            vhnbn.sort()
            return vhnbn

        ys = jificqy(yCoord)
        fcdq = -1
        tree = Fenwick(len(ys))

        def zjuzhjq(tqvai, jlqeqkj):
            def mhpkkke(vnibu, sbyg):
                if sbyg >= len(vnibu):
                    return len(vnibu)
                if sbyg <= vnibu[vnibu]:
                    return sbyg
                return mhpkkke(vnibu, sbyg + 1)
            # The above has an error in original pseudocode (vnibu[vnibu]), fix needed
            # Corrected binary search to find index of jlqeqkj in ys or next larger index
            vnibu = tqvai
            val = jlqeqkj
            left, right = 0, len(vnibu)
            while left < right:
                mid = (left + right) // 2
                if vnibu[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return left

        vusyk = zjuzhjq(ys, points[0][1]) + 1
        tree.add(vusyk)
        pre = {}

        def pxkitjl(oal, aoxy, oye, gsvnt):
            nonlocal fcdq
            if oal < len(points) - 1:
                x1, y1 = points[oal][0], points[oal][1]
                x2, y2 = points[oal + 1][0], points[oal + 1][1]

                mhej = zjuzhjq(ys, y2) + 1
                tree.add(mhej)

                if x1 != x2:
                    pxkitjl(oal + 1, aoxy, oye, gsvnt)
                    return

                cur = tree.query(zjuzhjq(ys, y1) + 1, mhej)
                if (y2 in pre) and (pre[y2][1] == y1) and (pre[y2][2] + 2 == cur):
                    uhvxxjr = max(gsvnt, (x2 - pre[y2][0]) * (y2 - y1))
                    pxkitjl(oal + 1, aoxy, uhvxxjr, gsvnt)
                    gsvnt = uhvxxjr
                    fcdq = gsvnt
                else:
                    pxkitjl(oal + 1, aoxy, gsvnt, gsvnt)
                pre[y2] = (x1, y1, cur)
            else:
                return

        pxkitjl(0, points, fcdq, fcdq)

        return fcdq