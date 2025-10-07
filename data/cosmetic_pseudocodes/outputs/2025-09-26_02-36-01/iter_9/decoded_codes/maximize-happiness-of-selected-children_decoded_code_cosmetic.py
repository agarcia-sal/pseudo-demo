class Solution:
    def maximumHappinessSum(self, ecstasy, limit):
        def arrangeDescending(arr):
            for position in range(1, len(arr)):
                key = arr[position]
                loc = position - 1
                while loc >= 0 and arr[loc] < key:
                    arr[loc + 1] = arr[loc]
                    loc -= 1
                arr[loc + 1] = key

        arrangeDescending(ecstasy)

        aggregate = 0
        subtractor = 0

        def iterateRecursively(idx):
            nonlocal aggregate, subtractor
            if idx > limit - 1:
                return
            temp_val = ecstasy[idx] - subtractor
            if temp_val < 0:
                temp_val = 0
            aggregate += temp_val
            subtractor += 1
            iterateRecursively(idx + 1)

        iterateRecursively(0)

        return aggregate