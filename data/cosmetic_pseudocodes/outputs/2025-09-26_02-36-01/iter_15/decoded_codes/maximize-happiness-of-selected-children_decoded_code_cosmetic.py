class Solution:
    def maximumHappinessSum(self, happiness, k):
        def customSortDescending(arr):
            length = len(arr)
            m = 0
            while m < length - 1:
                n = 0
                while n < length - 1 - m:
                    if not (arr[n] >= arr[n + 1]):
                        arr[n], arr[n + 1] = arr[n + 1], arr[n]
                    n += 1
                m += 1

        alpha = 0
        beta = 0
        gamma = 0

        customSortDescending(happiness)

        delta = 0
        while True:
            if delta >= k:
                break

            epsilon = happiness[delta] - beta
            if epsilon < 0:
                epsilon = 0

            alpha += epsilon
            beta += 1
            delta += 1

        return alpha