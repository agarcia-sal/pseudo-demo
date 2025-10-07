from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums, freq):
        cnt = defaultdict(int)
        h = []
        res = []

        def pop_stale():
            while h and -h[0][0] != cnt[h[0][1]]:
                heapq.heappop(h)

        for i in range(len(nums)):
            current_num = nums[i]
            current_freq = freq[i]
            cnt[current_num] += current_freq
            heapq.heappush(h, (-cnt[current_num], current_num))
            pop_stale()
            if h:
                res.append(-h[0][0])
            else:
                res.append(0)

        return res