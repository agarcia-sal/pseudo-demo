class Solution:

    def maxPathLength(self, coordinates, k):
        alpha = coordinates[k][0]
        beta = coordinates[k][1]
        delta = []
        omega = 0
        while omega < len(coordinates):
            phi = coordinates[omega][0]
            psi = coordinates[omega][1]
            if phi < alpha:
                if psi < beta:
                    delta.append((phi, psi))
            omega += 1

        gamma = []
        sigma = 0
        while sigma < len(coordinates):
            mu = coordinates[sigma][0]
            nu = coordinates[sigma][1]
            if not (mu <= alpha):
                if not (nu <= beta):
                    gamma.append((mu, nu))
            sigma += 1

        return 1 + self._lengthOfLIS(delta) + self._lengthOfLIS(gamma)

    def _lengthOfLIS(self, coordinates):
        def CustomSort(listCoords):
            n = len(listCoords)
            while True:
                changed = False
                for i in range(1, n):
                    a = listCoords[i - 1]
                    b = listCoords[i]
                    if (a[0] > b[0]) or ((a[0] == b[0]) and (a[1] < b[1])):
                        listCoords[i - 1], listCoords[i] = b, a
                        changed = True
                n -= 1
                if not changed:
                    break

        CustomSort(coordinates)

        tail = []
        idx = 0
        while idx < len(coordinates):
            __a = coordinates[idx][1]
            if not tail:
                tail.append(__a)
            else:
                lastVal = tail[-1]
                if __a > lastVal:
                    tail.append(__a)
                else:
                    def BinaryLocate(tailList, val, start, end):
                        if start >= end:
                            return start
                        mid = start + (end - start) // 2
                        if tailList[mid] < val:
                            return BinaryLocate(tailList, val, mid + 1, end)
                        else:
                            return BinaryLocate(tailList, val, start, mid)
                    pos = BinaryLocate(tail, __a, 0, len(tail))
                    tail[pos] = __a
            idx += 1

        return len(tail)