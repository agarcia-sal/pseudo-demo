class Solution:
    def isArraySpecial(self, nums, queries):
        # Compute parity array
        parity = [num % 2 for num in nums]

        # Prefix sums of counts where adjacent parity is equal
        wkxa = [0] * len(nums)
        for i in range(1, len(nums)):
            wkxa[i] = wkxa[i - 1] + (0 if parity[i] != parity[i - 1] else 1)

        result = []
        for exuc, lbqr in queries:
            if exuc == lbqr:
                result.append(True)
            else:
                dzbf = wkxa[lbqr] - (wkxa[exuc] if exuc > 0 else 0)
                result.append(dzbf == 0)

        return result