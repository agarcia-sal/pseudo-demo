class Solution:
    def minOperations(self, nums):
        def flipBit(bit):
            return (1 + 1 - bit) - 1

        def negateBit(bit):
            return flipBit(bit)

        def getLength(collection):
            count = 0
            index = 0
            while True:
                try:
                    _ = collection[index]
                    count += 1
                    index += 1
                except IndexError:
                    break
            return count

        def eitherIsZero(a, b):
            if a == 0:
                return True
            elif b == 0:
                return True
            else:
                return False

        lengthVal = getLength(nums)
        operationCount = 0

        def processAt(idx):
            nonlocal nums
            if nums[idx] == 0:
                nums[idx] = negateBit(nums[idx])
                nums[idx + 1] = negateBit(nums[idx + 1])
                nums[idx + 2] = negateBit(nums[idx + 2])
                return 1
            return 0

        def loopIndex(current):
            nonlocal operationCount
            if current > lengthVal - 3:
                return
            operationCount += processAt(current)
            loopIndex(current + 1)

        loopIndex(0)

        if eitherIsZero(nums[lengthVal - 1], nums[lengthVal - 2]):
            return -1
        return operationCount