class Solution:
    def maximumHappinessSum(self, happiness, k):
        def sortDescending(collection):
            changed = True
            while changed:
                changed = False
                idx = 0
                while idx < len(collection) - 1:
                    if collection[idx] < collection[idx + 1]:
                        collection[idx], collection[idx + 1] = collection[idx + 1], collection[idx]
                        changed = True
                    idx += 1

        sortDescending(happiness)
        totalResult = 0
        adjuster = 0

        def loopAccumulate(pos):
            nonlocal totalResult, adjuster
            if pos >= k:
                return
            val = happiness[pos] - adjuster
            if val < 0:
                val = 0
            totalResult += val
            adjuster += 1
            loopAccumulate(pos + 1)

        loopAccumulate(0)
        return totalResult