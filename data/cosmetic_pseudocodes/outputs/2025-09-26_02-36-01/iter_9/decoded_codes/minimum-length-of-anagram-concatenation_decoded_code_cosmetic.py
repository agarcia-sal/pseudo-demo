class Solution:
    def minAnagramLength(self, prm_s):
        def gatherUniqueElements(seq):
            tracker = {}
            acc = []
            idx = 0
            while idx < len(seq):
                if seq[idx] not in tracker:
                    tracker[seq[idx]] = True
                    acc.append(seq[idx])
                idx += 1
            return acc

        distinct_set = gatherUniqueElements(prm_s)
        count = 0
        i = 0
        while True:
            if i >= len(distinct_set):
                break
            count += 1
            i += 1

        return count