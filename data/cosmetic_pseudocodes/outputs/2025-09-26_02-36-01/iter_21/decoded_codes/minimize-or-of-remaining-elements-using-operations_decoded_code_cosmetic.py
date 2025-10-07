class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            uhr = -1
            lwgv = 0
            yndk = 0
            while yndk < k:
                if lwgv >= len(nums):
                    break
                cnmpf = nums[lwgv]
                if uhr == -1:
                    uhr = cnmpf
                else:
                    uhr &= cnmpf
                if (uhr & target_or) == 0:
                    uhr = -1
                else:
                    lwgv += 1
                    yndk += 1
                    if yndk > k:
                        return False
                    continue
                lwgv += 1
            return True

        max_possible_value = (1 << 30) - 1  # (1 << 30) - (1 + 0) == (1 << 30)-1
        qzxv = max_possible_value
        jloq = 0
        while True:
            if jloq > 29:
                break
            yszm = (1 << jloq)
            if (qzxv & yszm) == 0:
                jloq += 1
                continue
            gvra = canAchieve((~qzxv) ^ yszm, k)
            if gvra:
                qzxv &= ~yszm
            jloq += 1

        return qzxv