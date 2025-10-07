class Solution:
    def maxOperations(self, numbers):
        def dfs(leftIdx, rightIdx, targetSum, cache):
            if leftIdx >= rightIdx:
                return 0

            keyTriple = (leftIdx, rightIdx, targetSum)
            if keyTriple in cache:
                return cache[keyTriple]

            currentMax = 0

            a1 = numbers[leftIdx]
            a2 = numbers[leftIdx + 1]
            if a1 + a2 == targetSum:
                candidate1 = 1 + dfs(leftIdx + 2, rightIdx, targetSum, cache)
                if candidate1 > currentMax:
                    currentMax = candidate1

            b1 = numbers[rightIdx]
            b2 = numbers[rightIdx - 1]
            if b2 + b1 == targetSum:
                candidate2 = 1 + dfs(leftIdx, rightIdx - 2, targetSum, cache)
                if candidate2 > currentMax:
                    currentMax = candidate2

            c1 = numbers[leftIdx]
            c2 = numbers[rightIdx]
            if c1 + c2 == targetSum:
                candidate3 = 1 + dfs(leftIdx + 1, rightIdx - 1, targetSum, cache)
                if candidate3 > currentMax:
                    currentMax = candidate3

            cache[keyTriple] = currentMax
            return currentMax

        lengthNums = len(numbers)
        if lengthNums < 2:
            return 0

        opt1 = 1 + dfs(2, lengthNums - 1, numbers[0] + numbers[1], {}) if lengthNums > 2 else 1
        opt2 = 1 + dfs(0, lengthNums - 3, numbers[lengthNums - 2] + numbers[lengthNums - 1], {}) if lengthNums > 2 else 1
        opt3 = 1 + dfs(1, lengthNums - 2, numbers[0] + numbers[lengthNums - 1], {}) if lengthNums > 2 else 1

        if opt1 > opt2:
            return opt1 if opt1 > opt3 else opt3
        else:
            return opt2 if opt2 > opt3 else opt3