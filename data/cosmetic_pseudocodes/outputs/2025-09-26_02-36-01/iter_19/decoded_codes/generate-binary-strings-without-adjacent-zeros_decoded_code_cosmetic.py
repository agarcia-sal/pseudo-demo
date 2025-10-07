class Solution:
    def validStrings(self, count):
        resultCollection = []

        def explore(sequence):
            if len(sequence) == count:
                resultCollection.append(sequence)
                return
            lastChar = sequence[-1]
            if lastChar == '1':
                explore(sequence + '0')
                explore(sequence + '1')
            else:  # lastChar == '0'
                explore(sequence + '1')

        if count == 1:
            return ['0', '1']

        explore('0')
        explore('1')

        return resultCollection