class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)
        pc = 0
        ua = 0
        e = 0
        while ua < k:
            r = happiness[ua] - e
            if r < 0:
                r = 0
            pc += r
            e += 1
            ua += 1
        return pc