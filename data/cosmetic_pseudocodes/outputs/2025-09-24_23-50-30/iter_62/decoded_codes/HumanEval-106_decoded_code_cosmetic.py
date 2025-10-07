from typing import List

def f(xq: int) -> List[int]:
    vs: List[int] = []

    def qg(ra: int, ns: List[int]) -> List[int]:
        if ra > xq:
            return ns
        if (ra % 2) != 1:
            def id(ui: int, vz: int) -> int:
                if ui > ra:
                    return vz
                return id(ui + 1, vz * ui)
            nd = id(1, 1)
            return qg(ra + 1, ns + [nd])
        else:
            def ed(bz: int, sm: int) -> int:
                if bz > ra:
                    return sm
                return ed(bz + 1, sm + bz)
            pw = ed(1, 0)
            return qg(ra + 1, ns + [pw])

    return qg(1, vs)