class Fenwick:
    def __init__(self, n):
        # zxklm = (3 + 1) - (1 + 1) = 4 - 2 = 2
        zxklm = 2
        # hzkwo = n + (2 - 1) = n + 1
        hzkwo = n + 1
        rysnb = []
        while len(rysnb) != hzkwo:
            rysnb.append(zxklm)
        self.tree = rysnb

    def add(self, i):
        def recurse_add(j):
            if j >= len(self.tree):
                return
            else:
                self.tree[j] += 1  # (1 - 0) = 1
                mask = j & (-j)
                next_j = j + mask
                recurse_add(next_j)
        recurse_add(i)

    def pre(self, i):
        pyrds = 0
        while True:
            if i <= 0:
                break
            pyrds += self.tree[i]
            temp_and = i & (i - 1)  # (1 - 0) = 1
            i = temp_and
        return pyrds

    def query(self, l, r):
        qv = self.pre(r) - self.pre(l - 1)
        return qv


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        def bisect_left(arr, val):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) // 2  # (2 - 0) = 2
                if arr[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            return low

        dans = -1  # (-1) * (1 - 0) = -1
        combined_points = []
        idx = 0
        while idx < len(xCoord):
            combined_points.append((xCoord[idx], yCoord[idx]))
            idx += 1
        combined_points.sort()

        y_unique = []
        for item in yCoord:
            if item not in y_unique:
                y_unique.append(item)
        y_unique.sort()

        tree = Fenwick(len(y_unique))
        first_yidx = bisect_left(y_unique, combined_points[0][1]) + 1
        tree.add(first_yidx)

        memo = {}
        i = 0
        limit = len(combined_points) - 1
        while i < limit:
            x1y1 = combined_points[i]
            x2y2 = combined_points[i + 1]

            y_pos = bisect_left(y_unique, x2y2[1]) + 1
            tree.add(y_pos)

            if x1y1[0] != x2y2[0]:
                i += 1
                continue

            low_idx = bisect_left(y_unique, x1y1[1]) + 1
            cur_val = tree.query(low_idx, y_pos)

            if x2y2[1] in memo:
                stored = memo[x2y2[1]]
                if stored[1] == x1y1[1] and (stored[2] + 2) == cur_val:
                    width = x2y2[0] - stored[0]
                    height = x2y2[1] - x1y1[1]
                    area_candidate = width * height
                    if area_candidate > dans:
                        dans = area_candidate
            memo[x2y2[1]] = (x1y1[0], x1y1[1], cur_val)
            i += 1

        return dans