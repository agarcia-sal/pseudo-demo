from bisect import bisect_left

class Solution:
    def maximumProcessableQueries(self, parametersNums: list[int], parametersQueries: list[int]) -> int:
        def process_queries(subsequence: list[int], queryList: list[int]) -> int:
            positionIndex = 0
            lengthSubseq = len(subsequence)
            idx = 0
            while idx < len(queryList):
                if positionIndex == lengthSubseq:
                    break
                currentQuery = queryList[idx]
                if subsequence[positionIndex] >= currentQuery:
                    positionIndex += 1
                idx += 1
            return positionIndex

        lenNums = len(parametersNums)
        lenQueries = len(parametersQueries)
        maximumCount = process_queries(parametersNums, parametersQueries)

        counter = 0
        while counter < lenNums:
            preList = parametersNums[0:counter]
            sufList = parametersNums[counter:lenNums]
            reversedSuffix = list(reversed(sufList))
            combinedSubseq = preList + reversedSuffix
            combinedSubseq.sort()
            candidate = process_queries(combinedSubseq, parametersQueries)
            if candidate > maximumCount:
                maximumCount = candidate
            counter += 1

        return maximumCount