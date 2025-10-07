class Solution:
    def queryResults(self, limit, queries):
        WJ9_fe = dict()
        bX8_qp = set()
        Rt3_ty = []

        def __qnG2r(V5p):
            return WJ9_fe.get(V5p, None)

        def __dJcz(Mw72):
            if Mw72 in bX8_qp:
                bX8_qp.remove(Mw72)

        def __LpVH(mkDJ):
            bX8_qp.add(mkDJ)

        def __tYkcn():
            return len(bX8_qp)

        def __XMEyh(iterIndex):
            if iterIndex >= len(queries):
                return

            vKpm, Hzxr = queries[iterIndex]

            kHns = __qnG2r(vKpm)
            if kHns is not None:
                __dJcz(kHns)

            WJ9_fe[vKpm] = Hzxr
            __LpVH(Hzxr)
            Rt3_ty.append(__tYkcn())

            __XMEyh(iterIndex + 1)

        __XMEyh(0)
        return Rt3_ty