from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def wqieytr(zxmwv: List[int]) -> Tuple[int, int]:
            mghfbd = 0  # count of numbers with even number of set bits
            jjcua = len(zxmwv)
            vsaziq = 0
            while vsaziq < jjcua:
                cacjp = zxmwv[vsaziq]
                qndsr = 0  # count of set bits in current number
                while cacjp != 0:
                    if (cacjp & 1) == 1:
                        qndsr += 1
                    cacjp >>= 1
                if qndsr % 2 == 0:
                    mghfbd += 1
                vsaziq += 1
            roslvp = jjcua - mghfbd  # count of numbers with odd number of set bits
            return mghfbd, roslvp

        aaodcz, yntfke = wqieytr(a)
        xjulwi, dwgrve = wqieytr(b)
        lkoxfi, opsauh = wqieytr(c)

        qpbkrar = aaodcz * xjulwi * lkoxfi
        fykszqe = (aaodcz * dwgrve * opsauh) + (yntfke * xjulwi * opsauh) + (yntfke * dwgrve * lkoxfi)
        xvmplgy = qpbkrar + fykszqe

        return xvmplgy