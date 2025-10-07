class Solution:
    def minimumSubarrayLength(self, warp: list[int], threshold: int) -> int:
        def adjustTicker(ticker: list[int], figure: int, delta: int) -> None:
            flag = 1
            for counter in range(32):
                if figure & flag != 0:
                    ticker[counter] += delta
                flag <<= 1

        def determineOr(ticker: list[int]) -> int:
            acc = 0
            for idx in range(32):
                if ticker[idx] > 0:
                    acc |= (1 << idx)
            return acc

        total = len(warp)
        counterList = [0] * 32
        activeOr = 0
        startPos = 0
        bestLength = float('inf')

        endPos = 0
        while endPos < total:
            adjustTicker(counterList, warp[endPos], 1)
            activeOr |= warp[endPos]

            while activeOr >= threshold and startPos <= endPos:
                current_length = endPos - startPos + 1
                if bestLength > current_length:
                    bestLength = current_length
                adjustTicker(counterList, warp[startPos], -1)
                activeOr = determineOr(counterList)
                startPos += 1

            endPos += 1

        if bestLength == float('inf'):
            return -1
        else:
            return bestLength