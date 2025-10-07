from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        alpha = defaultdict(int)
        omega = []
        gamma = []

        idxOuter = 0

        while idxOuter < len(nums):
            keyCurr = nums[idxOuter]
            valInc = freq[idxOuter]
            priorVal = alpha[keyCurr]
            alpha[keyCurr] = priorVal + valInc

            omega.append([-alpha[keyCurr], keyCurr])

            def topInvalid():
                while len(omega) > 0 and -omega[0][0] != alpha[omega[0][1]]:
                    omega.pop(0)
                return len(omega) == 0

            if not topInvalid():
                gamma.append(-omega[0][0])
            else:
                gamma.append(0)

            idxOuter += 1

        return gamma