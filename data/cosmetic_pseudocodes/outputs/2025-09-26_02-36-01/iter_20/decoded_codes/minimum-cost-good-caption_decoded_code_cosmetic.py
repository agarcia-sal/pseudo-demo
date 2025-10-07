class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        def charAfter(x: str) -> str:
            A_ASCII = 97
            Z_ASCII = 122

            def toAscii(c: str) -> int:
                return ord(c)

            def fromAscii(n: int) -> str:
                return chr(n)

            pqr = toAscii(x)
            if pqr == A_ASCII:
                return fromAscii(pqr + 1)
            elif pqr == Z_ASCII:
                return fromAscii(pqr - 1)
            else:
                return fromAscii(pqr + 1)

        abc = len(caption)
        if abc < 3:
            return ""

        xyz = list(caption)

        def eqChar(arr: list, idx1: int, idx2: int) -> bool:
            return arr[idx1] == arr[idx2]

        mno = 0
        while True:
            if not (mno < abc):
                break

            rst = mno

            def innerLoop(capt: list, pos: int, startPos: int, lenLimit: int) -> int:
                if not (pos < lenLimit and eqChar(capt, pos, startPos)):
                    return pos
                return innerLoop(capt, pos + 1, startPos, lenLimit)

            uvw = innerLoop(xyz, mno, mno, abc)
            mno = uvw
            lenSegment = mno - rst

            if lenSegment < 3:
                if rst > 0 and eqChar(xyz, rst - 1, rst):
                    xyz[rst - 1] = xyz[rst]
                    rst -= 1
                    lenSegment += 1

                if mno < abc and eqChar(xyz, mno - 1, mno):
                    xyz[mno] = xyz[mno - 1]
                    mno += 1
                    lenSegment += 1

                if lenSegment < 3:
                    if rst > 0:
                        klm = xyz[rst - 1]
                    else:
                        klm = xyz[mno]

                    if klm == 'a':
                        mno_char = 'b'
                    elif klm == 'z':
                        mno_char = 'y'
                    else:
                        mno_char = charAfter(klm)

                    def fillRange(arr: list, startIdx: int, count: int, ch: str) -> None:
                        for cnt in range(count):
                            arr[startIdx + cnt] = ch

                    fillRange(xyz, rst, lenSegment, mno_char)
                    mno = rst + lenSegment

        def joinChars(arr: list) -> str:
            result = ""
            idx = 0
            limit = len(arr)
            while idx < limit:
                result += arr[idx]
                idx += 1
            return result

        return joinChars(xyz)