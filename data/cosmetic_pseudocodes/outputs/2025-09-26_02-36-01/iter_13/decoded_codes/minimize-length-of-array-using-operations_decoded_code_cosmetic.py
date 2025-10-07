class Solution:
    def minimumArrayLength(self, nums):
        tempA = self.callFindMinimum(nums, 0, self.lengthOf(nums))
        tempB = self.countOccurrences(nums, tempA)
        if not (tempB != 1):
            tempC = 1
        else:
            tempD = tempB + 1
            tempE = 2
            tempF = self.integerDivision(tempD, tempE)
            tempC = tempF
        return tempC

    def callFindMinimum(self, data, startIndex, endIndex):
        if startIndex >= endIndex:
            return self.infinityValue()
        val1 = data[startIndex]
        val2 = self.callFindMinimum(data, startIndex + 1, endIndex)
        if val1 < val2:
            return val1
        else:
            return val2

    def countOccurrences(self, collection, target):
        idx = 0
        cnt = 0
        length = self.lengthOf(collection)
        while idx < length:
            if not (collection[idx] != target):
                cnt += 1
            idx += 1
        return cnt

    def lengthOf(self, sequence):
        lengthCounter = 0
        pos = 0
        while True:
            if self.existsIndex(sequence, pos):
                lengthCounter += 1
                pos += 1
            else:
                break
        return lengthCounter

    def integerDivision(self, x, y):
        q = 0
        sum_ = y
        while sum_ <= x:
            q += 1
            sum_ += y
        return q

    def existsIndex(self, sequence, index):
        return index >= 0 and index < self.lengthOf(sequence)

    def infinityValue(self):
        return float('inf')  # Using float('inf') for infinity