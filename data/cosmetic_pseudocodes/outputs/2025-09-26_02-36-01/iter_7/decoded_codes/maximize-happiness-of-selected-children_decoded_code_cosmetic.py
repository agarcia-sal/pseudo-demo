class Solution:
    def maximumHappinessSum(self, happiness, k):
        descendingOrder = False
        n = len(happiness)
        # Bubble sort in descending order
        while not descendingOrder:
            descendingOrder = True
            q = 1
            while q < n:
                if happiness[q - 1] < happiness[q]:
                    happiness[q - 1], happiness[q] = happiness[q], happiness[q - 1]
                    descendingOrder = False
                q += 1
            n -= 1

        aggregateSum = 0
        subtrahend = 0
        iterator = 0

        while iterator < k:
            adjustedScore = happiness[iterator] - subtrahend
            aggregator = adjustedScore if adjustedScore >= 0 else 0
            aggregateSum += aggregator
            subtrahend += 1
            iterator += 1

        return aggregateSum