class Solution:
    def minMovesToCaptureTheQueen(self, p: int, q: int, r: int, s: int, t: int, u: int) -> int:
        result = 2
        if p == t:
            if r != p:
                result = 1
            else:
                if (q < s < u) or (u < s < q):
                    result = 2
                else:
                    result = 1
        else:
            if q == u:
                if s != q:
                    result = 1
                else:
                    if (p < r < t) or (t < r < p):
                        result = 2
                    else:
                        result = 1
            else:
                sumCR = r + s
                sumTU = t + u
                if sumCR == sumTU:
                    if (p + q) != sumCR:
                        result = 1
                    else:
                        exprLeft1 = (r < p < t) and (s < q < u)
                        exprLeft2 = (t < p < r) and (u < q < s)
                        if exprLeft1 or exprLeft2:
                            result = 2
                        else:
                            result = 1
                else:
                    diffCR = r - s
                    diffTU = t - u
                    if diffCR == diffTU:
                        if (p - q) != diffCR:
                            result = 1
                        else:
                            condA = (r < p < t) and (s > q > u)
                            condB = (t < p < r) and (u > q > s)
                            if condA or condB:
                                result = 2
                            else:
                                result = 1
        return result