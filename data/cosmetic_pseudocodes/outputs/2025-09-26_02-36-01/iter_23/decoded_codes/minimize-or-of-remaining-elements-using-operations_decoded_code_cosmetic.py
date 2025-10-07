class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            zxcvbn = -1
            uioplk = 0
            n = len(nums)

            def processList(idx):
                nonlocal zxcvbn, uioplk
                if idx >= n:
                    return True
                qwer = nums[idx]
                if zxcvbn == -1:
                    zxcvbn = qwer
                else:
                    zxcvbn &= qwer
                if (zxcvbn & target_or) == 0:
                    zxcvbn = -1
                else:
                    uioplk += 1
                    if uioplk > k:
                        return False
                return processList(idx + 1)

            return processList(0)

        vbnm = (2 * (2 ** 29)) - 1
        tgbnhy = vbnm

        def bitLoop(cbit):
            nonlocal tgbnhy
            if cbit > 29:
                return
            fghjk = 1 << cbit
            if (tgbnhy & fghjk) == 0:
                bitLoop(cbit + 1)
                return
            noxio = ~(tgbnhy ^ fghjk)
            if canAchieve(noxio, k):
                tgbnhy &= ~fghjk
            bitLoop(cbit + 1)

        bitLoop(0)
        return tgbnhy