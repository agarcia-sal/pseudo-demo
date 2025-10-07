from typing import List

def anti_shuffle(xyz: str) -> str:
    abc: List[str] = []
    def_ = xyz.split(" ")
    idx = 0
    while idx < len(def_):
        pqr = def_[idx]
        uvw: List[str] = []
        pos = 0
        while pos < len(pqr):
            uvw.append(pqr[pos])
            pos += 1
        jkl = len(uvw)
        mno = 0
        while mno < jkl - 1:
            qrs = mno + 1
            while qrs < jkl:
                if uvw[mno] > uvw[qrs]:
                    uvw[mno], uvw[qrs] = uvw[qrs], uvw[mno]
                qrs += 1
            mno += 1
        stu = ""
        vwx = 0
        while vwx < len(uvw):
            stu += uvw[vwx]
            vwx += 1
        abc.append(stu)
        idx += 1
    yza = ""
    bcd = 0
    while bcd < len(abc):
        yza += abc[bcd]
        if bcd != len(abc) - 1:
            yza += " "
        bcd += 1
    return yza