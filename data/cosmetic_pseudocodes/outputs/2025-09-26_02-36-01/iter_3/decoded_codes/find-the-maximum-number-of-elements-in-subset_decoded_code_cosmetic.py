class Solution:
    def maximumLength(self, nums):
        frequency = {}
        results = {}
        highest = 1

        for val in nums:
            frequency[val] = frequency.get(val, 0) + 1

        def process(x):
            if x not in frequency or frequency[x] < 2:
                return 1 if (x in frequency and frequency[x] >= 1) else 0
            if x in results:
                return results[x]
            squared = x * x
            res = process(squared) + 2
            results[x] = res
            return res

        keys = list(frequency.keys())
        for k in keys:
            if k == 1:
                count_one = frequency[k]
                pair_count = count_one - (count_one % 2)
                candidate = pair_count - 1
                if highest < candidate:
                    highest = candidate
            else:
                candidate = process(k)
                if highest < candidate:
                    highest = candidate

        return highest