class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        def buildOccurrenceIndices(arr, targetVal):
            return buildOccurrenceIndicesHelper(arr, targetVal, 0, [])

        def buildOccurrenceIndicesHelper(arr, targetVal, pos, acc):
            if pos >= len(arr):
                return acc
            newAcc = acc + [pos] if arr[pos] == targetVal else acc
            return buildOccurrenceIndicesHelper(arr, targetVal, pos + 1, newAcc)

        def processQueries(qList, occList, idx, res):
            if idx >= len(qList):
                return res
            valToAdd = occList[qList[idx] - 1] if qList[idx] <= len(occList) else -1
            return processQueries(qList, occList, idx + 1, res + [valToAdd])

        occurrencePositions = buildOccurrenceIndices(nums, x)
        finalResult = processQueries(queries, occurrencePositions, 0, [])
        return finalResult