class Solution:
    def maxTotalReward(self, cosmos):
        def mergeBitsets(p, q):
            return p | ((p & ((1 << q) - 1)) << q)

        container = sorted(set(cosmos))
        accumulator = 1

        for current in container:
            accumulator = mergeBitsets(accumulator, current)

        def bitLength(number):
            length = 0
            temp = number
            while temp > 0:
                temp >>= 1
                length += 1
            return length

        return bitLength(accumulator) - 1