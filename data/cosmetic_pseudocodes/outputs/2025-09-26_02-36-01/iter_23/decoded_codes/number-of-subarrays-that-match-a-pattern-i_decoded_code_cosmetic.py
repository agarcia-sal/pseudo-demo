class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        lenNums = len(nums)
        lenPattern = len(pattern)
        tally = 0

        def checkMatch(index, offset):
            if offset >= lenPattern:
                return True

            patElem = pattern[offset]
            currNum = nums[index + offset]
            nextNum = nums[index + offset + 1]

            if (patElem == 1 and not (nextNum > currNum)) or \
               (patElem == 0 and (nextNum != currNum)) or \
               (patElem == -1 and not (nextNum < currNum)):
                return False

            return checkMatch(index, offset + 1)

        position = 0
        while position <= lenNums - lenPattern - 1:
            if checkMatch(position, 0):
                tally += 1
            position += 1

        return tally