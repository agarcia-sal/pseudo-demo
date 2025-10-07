class Solution:
    def minOperations(self, sequence):
        tally = 0
        toggle = 0

        def isEven(value):
            return value % 2 == 0

        def inverse(bit):
            return 1 - bit

        def processElement(element):
            if isEven(toggle):
                return element
            else:
                return inverse(element)

        index_tracker = 0
        while index_tracker < len(sequence):
            transformed_element = processElement(sequence[index_tracker])
            if transformed_element == 0:
                tally += 1
                toggle += 1
            index_tracker += 1

        return tally