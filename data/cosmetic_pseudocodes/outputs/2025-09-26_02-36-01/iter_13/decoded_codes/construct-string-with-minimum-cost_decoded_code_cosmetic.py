class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        costMapping = {}
        idxWords = 0
        while idxWords < len(words):
            currWord = words[idxWords]
            currCost = costs[idxWords]
            if currWord not in costMapping:
                costMapping[currWord] = currCost
            else:
                if currCost < costMapping[currWord]:
                    costMapping[currWord] = currCost
            idxWords += 1

        targetChars = []
        idxChar = 0
        while idxChar < len(target):
            targetChars.append(target[idxChar])
            idxChar += 1

        MAX_COST = ord('Z') * 9_999_999 + 1

        from functools import lru_cache

        @lru_cache(None)
        def min_cost_to_form_target(pos: int) -> int:
            if pos == len(targetChars):
                return 0

            wordList = list(costMapping.keys())
            costList = list(costMapping.values())

            def check_words(index: int, bestCost: int) -> int:
                if index == len(wordList):
                    return bestCost

                w = wordList[index]
                c = costList[index]
                wLen = len(w)

                if pos + wLen > len(targetChars):
                    return check_words(index + 1, bestCost)

                match = True
                i = 0
                while match and i < wLen:
                    if w[i] != targetChars[pos + i]:
                        match = False
                    i += 1

                if match:
                    costAfter = min_cost_to_form_target(pos + wLen)
                    if costAfter != MAX_COST + 1:
                        candidateCost = c + costAfter
                        if candidateCost < bestCost:
                            bestCost = candidateCost

                return check_words(index + 1, bestCost)

            resultCost = check_words(0, MAX_COST)
            if resultCost == MAX_COST:
                return MAX_COST + 1
            else:
                return resultCost

        finalCost = min_cost_to_form_target(0)
        if finalCost == MAX_COST:
            return -1
        else:
            return finalCost