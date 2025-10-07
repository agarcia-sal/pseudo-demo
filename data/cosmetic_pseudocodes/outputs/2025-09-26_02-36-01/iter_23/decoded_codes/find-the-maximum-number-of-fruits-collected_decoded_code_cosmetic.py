class Solution:
    def maxCollectedFruits(self, fruits):
        M = len(fruits)

        V0 = [(1, 1), (1, 0)]
        V1 = [(1, 0), (1, -1), (1, 1)]
        V2 = [(-1, 1), (0, 1), (1, 1)]

        Cache = {}

        def Explore(a0, b0, a1, b1, a2, b2):
            def BoundCheck(p, q):
                return not (0 <= p < M and 0 <= q < M)

            if BoundCheck(a0, b0) or BoundCheck(a1, b1) or BoundCheck(a2, b2):
                return -(2 ** 31)

            if a0 == b0 == a1 == b1 == a2 == b2 == M - 1:
                return fruits[M - 1][M - 1]

            Key = (a0, b0, a1, b1, a2, b2)
            if Key in Cache:
                return Cache[Key]

            # Calculate Tally
            Tally = fruits[a0][b0]
            if (a0 == a1 and b0 == b1) or (a0 == a2 and b0 == b2):
                Tally = 0

            if a1 == a2 and b1 == b2:
                Tally += fruits[a1][b1]
            else:
                Tally += fruits[a1][b1] + fruits[a2][b2]

            MaxCollect = -(2 ** 31)
            i0 = 0

            def NextDir0():
                nonlocal i0, MaxCollect
                if i0 >= len(V0):
                    return MaxCollect
                dX0, dY0 = V0[i0]
                i1 = 0

                def NextDir1():
                    nonlocal i1, i0, MaxCollect
                    if i1 >= len(V1):
                        i0 += 1
                        return NextDir0()
                    dX1, dY1 = V1[i1]
                    i2 = 0

                    def NextDir2():
                        nonlocal i2, i1, MaxCollect
                        if i2 >= len(V2):
                            i1 += 1
                            return NextDir1()
                        dX2, dY2 = V2[i2]

                        Candidate = Explore(a0 + dX0, b0 + dY0, a1 + dX1, b1 + dY1, a2 + dX2, b2 + dY2)
                        if Candidate > MaxCollect:
                            MaxCollect = Candidate

                        i2 += 1
                        return NextDir2()

                    return NextDir2()

                return NextDir1()

            MaxCollect = NextDir0()
            Cache[Key] = Tally + MaxCollect
            return Tally + MaxCollect

        return Explore(0, 0, 0, M - 1, M - 1, 0)