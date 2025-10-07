class Solution:
    def minAnagramLength(self, s):
        def buildSetFromString(string, res_set):
            idx = 0
            while idx < len(string):
                if string[idx] not in res_set:
                    res_set.add(string[idx])
                idx += 1

        accumulator = set()
        buildSetFromString(s, accumulator)

        def computeSetSize(se):
            count = 0
            iterator = iter(se)
            while True:
                try:
                    element = next(iterator)
                except StopIteration:
                    break
                count += 1
            return count

        return computeSetSize(accumulator)