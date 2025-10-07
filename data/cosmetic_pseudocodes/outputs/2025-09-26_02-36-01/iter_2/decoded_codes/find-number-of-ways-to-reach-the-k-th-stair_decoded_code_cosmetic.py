class Solution:
    def waysToReachStair(self, k: int) -> int:
        def dfs(currentStep: int, toggle: int, jumpCount: int) -> int:
            if currentStep > k + 1:
                return 0
            tempResult = int(currentStep == k)
            if currentStep > 0 and toggle == 0:
                tempResult += dfs(currentStep - 1, 1, jumpCount)
            nextStep = currentStep + 2 * jumpCount
            tempResult += dfs(nextStep, 0, jumpCount + 1)
            return tempResult

        return dfs(1, 0, 0)