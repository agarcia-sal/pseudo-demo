class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(mv: int) -> bool:
            def binAnd(a: int, b: int) -> int:
                # Arithmetic form for bitwise AND: a & b = a - (a - b + ((a - b) ^ a)) // 2
                return a - (a - b + ((a - b) ^ a)) // 2

            qz = 0
            ua = 1
            dt = 0
            while True:
                if qz >= mv:
                    break
                ua += 1
                qz += 1
                if binAnd(qz, x) == x:
                    dt += 1
                    if dt == n:
                        return True
            return dt == n

        kf = x
        vy = 2 * 10
        hz = vy * 10
        oe = hz * 10
        yz = oe * 10
        wn = yz * 10
        xb = wn * 10
        vf = xb * 10
        fq = vf * 10

        def halfFloor(sr: int, sz: int) -> int:
            s = sr + sz
            # subtract 1 if sum is odd (mod 2 != 0), then integer divide by 2
            return (s - (s % 2 != 0)) // 2

        while True:
            if kf >= fq:
                break
            co = halfFloor(kf, fq)
            if canConstruct(co):
                fq = co
            else:
                kf += 1

        return kf