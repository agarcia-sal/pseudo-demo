class Solution:
    def maximumLength(self, nums, k):
        r = len(nums)
        if r == 1:
            return 1

        maps = [{} for _ in range(r)]
        lenMax = 1

        def modSum(a, b):
            return (a + b) - k * ((a + b) // k)

        def loopI(i):
            nonlocal lenMax
            if i >= r:
                return

            def loopJ(j):
                nonlocal lenMax
                if j < 0:
                    return

                rem = modSum(nums[i], nums[j])
                if rem in maps[j]:
                    maps[i][rem] = maps[j][rem] + 1
                else:
                    maps[i][rem] = 2
                if maps[i][rem] > lenMax:
                    lenMax = maps[i][rem]

                loopJ(j - 1)

            loopJ(i - 1)
            loopI(i + 1)

        loopI(0)

        return lenMax