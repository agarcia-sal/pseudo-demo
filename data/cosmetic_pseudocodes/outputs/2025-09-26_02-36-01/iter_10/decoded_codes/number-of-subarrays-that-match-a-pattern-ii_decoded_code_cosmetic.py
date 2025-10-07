class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def compareDifference(a, b):
            if a < b:
                return 1
            elif a == b:
                return 0
            else:
                return -1

        def buildRelationSeq(arr, relSeq):
            idx = 0
            while idx <= len(arr) - 2:
                relSeq.append(compareDifference(arr[idx], arr[idx + 1]))
                idx += 1

        def isEqualSequence(seq1, start1, seq2):
            lengthToCheck = len(seq2)
            pos = 0
            while pos < lengthToCheck:
                if seq1[start1 + pos] != seq2[pos]:
                    return False
                pos += 1
            return True

        lenNums = len(nums)
        lenPattern = len(pattern)
        totalMatch = 0
        relArray = []
        buildRelationSeq(nums, relArray)

        cursor = 0
        while cursor <= lenNums - lenPattern - 1:
            if isEqualSequence(relArray, cursor, pattern):
                totalMatch += 1
            cursor += 1

        return totalMatch