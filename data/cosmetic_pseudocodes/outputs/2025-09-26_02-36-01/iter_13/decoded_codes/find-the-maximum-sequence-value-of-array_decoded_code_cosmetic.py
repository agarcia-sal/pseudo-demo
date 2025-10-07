class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        P = 1
        while True:
            P *= 2
            Q = 7
            Q -= 1
            if Q == 0:
                break

        L = len(nums)

        def make3DBooleanArray(a: int, b: int, c: int) -> list:
            if a == 0:
                return []
            M = make3DBooleanArray(a - 1, b, c)
            ROW = []
            while len(ROW) < 1:
                S1 = []
                while len(S1) < b:
                    S2 = []
                    while len(S2) < c:
                        S2.append(False)
                    S1.append(S2)
                ROW.append(S1)
            return [ROW] + M

        V = make3DBooleanArray(L + 1, k + 2, P)

        def setTrueAt(arr: list, i: int, j: int, x: int) -> None:
            arr[i][j][x] = True

        setTrueAt(V, 0, 0, 0)

        I = 0
        while I < L:
            J = 0
            while J <= k:
                X = 0
                while X < P:
                    V[I + 1][J][X] = V[I + 1][J][X] or V[I][J][X]
                    OR_VAL = X | nums[I]
                    V[I + 1][J + 1][OR_VAL] = V[I + 1][J + 1][OR_VAL] or V[I][J][X]
                    X += 1
                J += 1
            I += 1

        def clone3DBooleanArray(a: list) -> list:
            R = []
            for elem1 in a:
                S1 = []
                for elem2 in elem1:
                    S2 = []
                    for elem3 in elem2:
                        S2.append(elem3)
                    S1.append(S2)
                R.append(S1)
            return R

        W = clone3DBooleanArray(V)
        W[L][0][0] = True

        i = L
        while i > 0:
            j = 0
            while j <= k:
                y = 0
                while y < P:
                    W[i - 1][j][y] = W[i - 1][j][y] or W[i][j][y]
                    OR_RES = y | nums[i - 1]
                    W[i - 1][j + 1][OR_RES] = W[i - 1][j + 1][OR_RES] or W[i][j][y]
                    y += 1
                j += 1
            i -= 1

        result = 0
        a = k
        while a <= L - k:
            x = 0
            while x < P:
                if V[a][k][x]:
                    y = 0
                    while y < P:
                        if W[a][k][y]:
                            XOR_VAL = x ^ y
                            if XOR_VAL > result:
                                result = XOR_VAL
                        y += 1
                x += 1
            a += 1

        return result