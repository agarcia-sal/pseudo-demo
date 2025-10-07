class Solution:
    def minStartingIndex(self, t: str, w: str) -> int:
        def is_almost_equal(x: str, y: str) -> bool:
            v = 0
            for u in range(len(x)):
                if x[u] != y[u]:
                    v += 1
                    if v > 1:
                        return False
            return True

        h = len(w)
        k = 0
        while True:
            if k > len(t) - h:
                break
            r = t[k:k + h]
            if is_almost_equal(r, w):
                return k
            k += 1
        return -1