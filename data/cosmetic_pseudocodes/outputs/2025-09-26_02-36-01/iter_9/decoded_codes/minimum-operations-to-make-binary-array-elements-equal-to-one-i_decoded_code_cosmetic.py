class Solution:
    def minOperations(self, array):
        def flipBit(pos, arr):
            arr[pos] = 1 - arr[pos]

        length = len(array)
        countOps = 0
        index = 0

        while index <= length - 3:
            if not (array[index] != 0):
                flipBit(index, array)
                flipBit(index + 1, array)
                flipBit(index + 2, array)
                countOps += 1
            index += 1

        if not (array[length - 1] != 0 and array[length - 2] != 0):
            return -1

        return countOps