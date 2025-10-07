class Solution:
    def maximumTotalDamage(self, power):
        def recProcess(pos, uniqPwr, freqMap, memo):
            if pos < 0:
                return 0
            if pos in memo:
                return memo[pos]

            currPwr = uniqPwr[pos]
            exclVal = recProcess(pos - 1, uniqPwr, freqMap, memo)

            incVal = currPwr * freqMap[currPwr]
            checkIdx = pos - 1
            while checkIdx >= 0 and uniqPwr[checkIdx] >= currPwr - 2:
                checkIdx -= 1

            if checkIdx >= 0:
                incVal += recProcess(checkIdx, uniqPwr, freqMap, memo)

            resultVal = incVal if incVal > exclVal else exclVal
            memo[pos] = resultVal
            return resultVal

        frequencyMapping = {}
        for element in power:
            frequencyMapping[element] = frequencyMapping.get(element, 0) + 1

        distinctPowers = sorted(frequencyMapping.keys())

        dynamicProgMemo = {}
        finalMaxDamage = recProcess(len(distinctPowers) - 1, distinctPowers, frequencyMapping, dynamicProgMemo)
        return finalMaxDamage