class Solution:
    def maximumScore(self, grid):
        n = len(grid)
        # prefix[c+1][r]: cumulative sum of grid[r][0..c]
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        prevPick = [0] * (n + 1)
        prevSkip = [0] * (n + 1)

        def computePrefixRow(r, c):
            if c > n - 1:
                return
            prefix[c + 1][r] = prefix[c][r] + grid[r][c]
            computePrefixRow(r, c + 1)

        def computePrefixCol(j):
            if j > n - 1:
                return
            computePrefixRow(j, 0)
            computePrefixCol(j + 1)

        computePrefixCol(0)

        def innerLoop(curr, prev, j, currPick, currSkip):
            if prev > n:
                return
            if curr > n:
                innerLoop(0, prev + 1, j, currPick, currSkip)
                return
            if curr > prev:
                score = prefix[j - 1][curr] - prefix[j - 1][prev]
                currPick[curr] = max(currPick[curr], prevSkip[prev] + score)
                currSkip[curr] = max(currSkip[curr], prevSkip[prev] + score)
            else:
                score = prefix[j][prev] - prefix[j][curr]
                currPick[curr] = max(currPick[curr], prevPick[prev] + score)
                currSkip[curr] = max(currSkip[curr], prevPick[prev])
            innerLoop(curr + 1, prev, j, currPick, currSkip)

        def outerLoop(j):
            nonlocal prevPick, prevSkip
            if j > n - 1:
                return
            currPick = [0] * (n + 1)
            currSkip = [0] * (n + 1)
            innerLoop(0, 0, j, currPick, currSkip)
            prevPick = currPick
            prevSkip = currSkip
            outerLoop(j + 1)

        outerLoop(1)

        maxVal = prevPick[0]
        i = 1
        while i <= n:
            if prevPick[i] > maxVal:
                maxVal = prevPick[i]
            i += 1

        return maxVal