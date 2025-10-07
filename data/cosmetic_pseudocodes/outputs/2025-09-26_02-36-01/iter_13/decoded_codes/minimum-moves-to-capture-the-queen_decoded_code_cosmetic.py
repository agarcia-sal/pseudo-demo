class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        # If the rook and queen share the same column
        if not (a != e):
            if c == a:
                if not ((b < d < f) or (f < d < b)):
                    return 1
                else:
                    return 2
            else:
                return 1

        # If the rook and queen share the same row
        if not (b != f):
            if d == b:
                if not ((a < c < e) or (e < c < a)):
                    return 1
                else:
                    return 2
            else:
                return 1

        # If rook and queen are on the same / diagonal (sum of coords equal)
        if (c + d) == (e + f):
            if (a + b) != (c + d):
                return 1
            else:
                if not (((c < a < e and d < b < f) or (e < a < c and f < b < d))):
                    return 1
                else:
                    return 2

        # If rook and queen are on the same \ diagonal (difference of coords equal)
        if (c - d) == (e - f):
            if (a - b) != (c - d):
                return 1
            else:
                if not (((c < a < e and d > b > f) or (e < a < c and f > b > d))):
                    return 1
                else:
                    return 2

        # If none of the conditions above hold, it takes 2 moves
        return 2