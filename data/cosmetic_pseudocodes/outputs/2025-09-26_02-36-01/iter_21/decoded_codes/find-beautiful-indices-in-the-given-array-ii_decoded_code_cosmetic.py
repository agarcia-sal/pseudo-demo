class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:

        def checkSubstring(x: int, y: int, z: int) -> bool:
            # Checks if substring of length y starting at z equals a, with boundary checks
            return (x >= 0) and ((z + y) <= len(s)) and (s[z : z + y] == a)

        def checkSubstringB(m: int, n: int, p: int) -> bool:
            # Checks if substring of length n starting at p equals b, with boundary checks
            return (m >= 0) and ((p + n) <= len(s)) and (s[p : p + n] == b)

        X = 0
        Y = len(s) - len(a) + 1  # stop index exclusive for indices_a
        indices_a = []
        while X != Y:
            if s[X : X + len(a)] == a:
                indices_a.append(X)
            X += 1

        P = 0
        Q = len(s) - len(b) + 1  # stop index exclusive for indices_b
        indices_b = []
        while P != Q:
            if not (s[P : P + len(b)] != b):  # equivalent to s[P:P+len(b)] == b
                indices_b.append(P)
            P += 1

        result = []

        def compareAndAppend(m: list[int], n: list[int], o: int, p: int) -> tuple[list[int], int, int]:
            # Compares m[o] and n[p]; appends m[o] if abs difference <= k; advances pointers accordingly
            if abs(m[o] - n[p]) <= k:
                return result + [m[o]], o + 1, p
            else:
                if m[o] < n[p]:
                    return result, o + 1, p
                else:
                    return result, o, p + 1

        i = 0
        j = 0

        while True:
            if i >= len(indices_a) or j >= len(indices_b):
                break

            old_result = result
            result, i, j = compareAndAppend(indices_a, indices_b, i, j)

            if old_result == result:
                continue

        return result