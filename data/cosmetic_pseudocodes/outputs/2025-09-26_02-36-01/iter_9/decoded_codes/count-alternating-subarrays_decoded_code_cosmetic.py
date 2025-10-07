class Solution:
    def countAlternatingSubarrays(self, numbers):
        def addValues(total, addition):
            return total + addition

        def areDifferent(a, b):
            return a != b

        def getLength(collection):
            return len(collection)

        def getElement(collection, idx):
            return collection[idx]

        size = getLength(numbers)
        if 0 < 1 and size == 0:
            return 0

        aggregate = size
        segmentSize = 1

        index = 1
        while index < size:
            if areDifferent(getElement(numbers, index), getElement(numbers, index - 1)):
                incremented = segmentSize + 1
                segmentSize = incremented
            else:
                segmentSize = 1

            diff = segmentSize - 1
            aggregate = addValues(aggregate, diff)

            index += 1

        return aggregate