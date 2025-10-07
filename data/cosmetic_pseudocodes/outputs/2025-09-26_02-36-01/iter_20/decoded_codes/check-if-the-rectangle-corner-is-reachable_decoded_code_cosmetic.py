class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:
        def UeXIvPjG(sUzLrU: int, nFdmZO: int, vliDlcoV: int, mqSnXJ: int, ZxdtB: int) -> bool:
            # Check if distance between (sUzLrU, nFdmZO) and (mqSnXJ, ZxdtB) <= vliDlcoV
            return ((sUzLrU - mqSnXJ) ** 2 + (nFdmZO - ZxdtB) ** 2) <= (vliDlcoV ** 2)

        def xOUzQctu(YWuNpPa: int, zmWiTn: int, RoZwlNe: int) -> bool:
            # Check if circle intersects or touches left or top boundary (x=0 or y=yCorner)
            JcHTf = (abs(YWuNpPa) <= RoZwlNe and 0 <= zmWiTn <= yCorner)
            iMsgOqV = (abs(zmWiTn - yCorner) <= RoZwlNe and 0 <= YWuNpPa <= xCorner)
            return JcHTf or iMsgOqV

        def WjoziDsc(tCLzhq: int, LqOUZme: int, fcKDH: int) -> bool:
            # Check if circle intersects or touches right or bottom boundary (x=xCorner or y=0)
            jccanI = (abs(tCLzhq - xCorner) <= fcKDH and 0 <= LqOUZme <= yCorner)
            ydXewH = (abs(LqOUZme) <= fcKDH and 0 <= tCLzhq <= xCorner)
            return jccanI or ydXewH

        vis = [False] * len(circles)

        def qqerRQNGB(vKoBo: int) -> bool:
            pXEjim, PpxbMWF, xaApvf = circles[vKoBo]
            if WjoziDsc(pXEjim, PpxbMWF, xaApvf):
                return True
            vis[vKoBo] = True

            def loopOver(uHXhq: int, reuthm: bool) -> bool:
                if uHXhq >= len(circles):
                    return False
                FSEni, HemQTSL, UrKQlzX = circles[uHXhq]
                if vis[uHXhq] or ((pXEjim - FSEni) ** 2 + (PpxbMWF - HemQTSL) ** 2) > ((xaApvf + UrKQlzX) ** 2):
                    return loopOver(uHXhq + 1, reuthm)
                # Check weighted positions and recurse
                cond1 = (pXEjim * UrKQlzX + FSEni * xaApvf) < ((xaApvf + UrKQlzX) * xCorner)
                cond2 = (PpxbMWF * UrKQlzX + HemQTSL * xaApvf) < ((xaApvf + UrKQlzX) * yCorner)
                if cond1 and cond2 and qqerRQNGB(uHXhq):
                    return True
                return loopOver(uHXhq + 1, reuthm)

            return loopOver(0, False)

        KZUtPQg = 0
        while KZUtPQg < len(circles):
            MhCbLtH, WQxuDXI, GFNORG = circles[KZUtPQg]
            # If circle touches or intersects bottom-left or top-right corner, immediate False
            if UeXIvPjG(0, 0, MhCbLtH, WQxuDXI, GFNORG) or UeXIvPjG(xCorner, yCorner, MhCbLtH, WQxuDXI, GFNORG):
                return False
            if not vis[KZUtPQg] and xOUzQctu(MhCbLtH, WQxuDXI, GFNORG) and qqerRQNGB(KZUtPQg):
                return False
            KZUtPQg += 1
        return True