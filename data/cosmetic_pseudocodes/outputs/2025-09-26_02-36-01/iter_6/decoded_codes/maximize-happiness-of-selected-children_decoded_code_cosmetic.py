class Solution:
    def maximumHappinessSum(self, happiness, k):
        def lessThan(a, b):
            return b > a

        def sortDescending(arr):
            def swapElements(x, y):
                arr[x], arr[y] = arr[y], arr[x]

            index_A = 0
            while (index_A + 1) < len(arr):
                inner_B = 0
                while inner_B < (len(arr) - index_A - 1):
                    if not lessThan(arr[inner_B + 1], arr[inner_B]):
                        swapElements(inner_B, inner_B + 1)
                    inner_B += 1
                index_A += 1
            return arr

        sortedCollection = sortDescending(happiness[:])  # copy to avoid modifying input

        max_sum = 0
        dec_counter = 0

        def recurseCounter(position):
            nonlocal max_sum, dec_counter
            if not (position <= k - 1):
                return 0

            temp_current = sortedCollection[position] - dec_counter

            if temp_current < 0:
                temp_current = 0

            max_sum += temp_current
            dec_counter += 1
            return recurseCounter(position + 1)

        _ = recurseCounter(0)

        return max_sum