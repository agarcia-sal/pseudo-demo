class Solution:
    def canSortArray(self, array):
        def countSetBits(value):
            bitCount = 0
            tempVal = value
            while tempVal != 0:
                bitCount += tempVal & 1
                tempVal >>= 1
            return bitCount

        lengthArray = len(array)
        target = sorted(array)

        indexOuter = 0
        while indexOuter < lengthArray - 1:
            indexInner = 0
            while indexInner < lengthArray - 1:
                leftVal = array[indexInner]
                rightVal = array[indexInner + 1]
                leftBits = countSetBits(leftVal)
                rightBits = countSetBits(rightVal)
                if leftBits == rightBits and leftVal > rightVal:
                    array[indexInner], array[indexInner + 1] = rightVal, leftVal
                indexInner += 1
            indexOuter += 1

        return array == target