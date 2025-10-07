from math import inf

class Solution:
    def minimumCost(self, target, words, costs):
        storageMap = {}
        for i in range(len(words)):
            currentKey = words[i]
            currentVal = costs[i]
            if currentKey not in storageMap or currentVal < storageMap[currentKey]:
                storageMap[currentKey] = currentVal

        targetChars = list(target)
        memo = {}

        def helperFunc(position):
            if position >= len(targetChars):
                return 0
            if position in memo:
                return memo[position]

            leastCost = inf
            for wordStr, wordVal in storageMap.items():
                wl = len(wordStr)
                if position + wl <= len(targetChars):
                    segment = targetChars[position:position + wl]
                    if segment == list(wordStr):
                        remainingCost = helperFunc(position + wl)
                        if remainingCost != inf:
                            totalCost = wordVal + remainingCost
                            if totalCost < leastCost:
                                leastCost = totalCost

            memo[position] = leastCost
            return leastCost

        totalCost = helperFunc(0)
        return totalCost if totalCost != inf else -1