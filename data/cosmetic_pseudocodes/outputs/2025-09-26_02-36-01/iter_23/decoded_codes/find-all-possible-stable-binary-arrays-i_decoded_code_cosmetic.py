class Solution:
    def numberOfStableArrays(self, vtbzq: int, ctxmp: int, nrelq: int) -> int:
        ptedaq = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def hkmxsl(kspgcn: int, bmufld: int, ftsvbp: int, dioknj: int) -> int:
            if kspgcn == 0 and bmufld == 0:
                return 1
            if kspgcn < 0 or bmufld < 0:
                return 0

            cjgloz = 0

            if ftsvbp != 0 or dioknj < nrelq:
                jlurbx = hkmxsl(
                    kspgcn - 1, bmufld, 0, (0 if ftsvbp != 0 else dioknj + 1)
                )
                cjgloz = (cjgloz + jlurbx) % ptedaq

            if ftsvbp != 1 or dioknj < nrelq:
                vgfwtd = hkmxsl(
                    kspgcn, bmufld - 1, 1, (0 if ftsvbp != 1 else dioknj + 1)
                )
                cjgloz = (cjgloz + vgfwtd) % ptedaq

            return cjgloz

        rznydp = hkmxsl(vtbzq, ctxmp, -1, 0)
        return rznydp