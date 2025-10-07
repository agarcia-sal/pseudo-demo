class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        result = 0
        alpha = 0
        beta = 0
        heightCount = 1
        widthCount = 1

        # Sort in descending order using built-in sort for efficiency
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        while alpha < len(horizontalCut) or beta < len(verticalCut):
            if beta == len(verticalCut) or (alpha < len(horizontalCut) and horizontalCut[alpha] > verticalCut[beta]):
                incrementVal = horizontalCut[alpha]
                addVal = incrementVal * widthCount
                result += addVal
                heightCount += 1
                alpha += 1
            else:
                incrementVal = verticalCut[beta]
                addVal = incrementVal * heightCount
                result += addVal
                widthCount += 1
                beta += 1

        return result