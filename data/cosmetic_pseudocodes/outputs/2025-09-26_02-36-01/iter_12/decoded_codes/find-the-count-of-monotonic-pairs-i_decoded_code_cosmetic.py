class Solution:
    def countOfPairs(self, nums):
        BigMod = 10**9 + 7
        lengthN = len(nums)

        def findMax(lst):
            tempMax = lst[0]
            for v in lst:
                if v > tempMax:
                    tempMax = v
            return tempMax

        highest = findMax(nums)

        # Initialize 3D table: lengthN x (highest+1) x (highest+1) with zeros
        table = [[[0] * (highest + 1) for _ in range(highest + 1)] for _ in range(lengthN)]

        x = 0
        while x <= nums[0]:
            y = nums[0] - x
            table[0][x][y] = 1
            x += 1

        for iRow in range(1, lengthN):
            for jRow in range(nums[iRow] + 1):
                kRow = nums[iRow] - jRow
                for jPrev in range(jRow + 1):
                    for kPrev in range(kRow, highest + 1):
                        addVal = table[iRow - 1][jPrev][kPrev]
                        table[iRow][jRow][kRow] += addVal
                        if table[iRow][jRow][kRow] >= BigMod:
                            table[iRow][jRow][kRow] %= BigMod

        sumResult = 0
        last_val = nums[-1]
        for jSum in range(highest + 1):
            for kSum in range(highest + 1):
                if jSum + kSum == last_val:
                    sumResult += table[lengthN - 1][jSum][kSum]
                    if sumResult >= BigMod:
                        sumResult %= BigMod

        return sumResult