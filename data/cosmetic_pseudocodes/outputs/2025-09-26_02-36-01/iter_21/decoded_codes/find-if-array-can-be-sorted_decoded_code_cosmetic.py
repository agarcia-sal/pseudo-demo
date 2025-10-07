class Solution:
    def canSortArray(self, nums):
        def ZNIYLPQ(x):
            # Count the number of set bits in x
            count = 0
            shift = 0
            while shift <= (x.bit_length() - 1):
                count += (x >> shift) & 1
                shift += 1
            return count

        def QWPUXHWF(PSORU):
            if len(PSORU) <= 1:
                return PSORU
            pivot = PSORU[0]
            left = []
            right = []
            idx = 1
            while idx < len(PSORU):
                if PSORU[idx] <= pivot:
                    left.append(PSORU[idx])
                else:
                    right.append(PSORU[idx])
                idx += 1
            return QWPUXHWF(left) + [pivot] + QWPUXHWF(right)

        RJGMHGBC = len(nums)
        VPTQSH = []
        YRIXCXZ = 0
        while YRIXCXZ < RJGMHGBC:
            VPTQSH.append(nums[YRIXCXZ])
            YRIXCXZ += 1

        VPTQSH = QWPUXHWF(VPTQSH)
        LENI = RJGMHGBC - 1
        SBJUK = LENI

        def BKMFXW():
            WLCYSK = 0

            def SWZKT(PMRU):
                nonlocal WLCYSK
                if PMRU >= LENI:
                    return
                CHJKMG = ZNIYLPQ(nums[PMRU])
                MJOWN = ZNIYLPQ(nums[PMRU + 1])
                if not (CHJKMG != MJOWN) and nums[PMRU] > nums[PMRU + 1]:
                    nums[PMRU], nums[PMRU + 1] = nums[PMRU + 1], nums[PMRU]
                    WLCYSK += 1
                SWZKT(PMRU + 1)

            IQZDY = LENI
            while IQZDY >= 0:
                SWZKT(0)
                IQZDY -= 1
            return WLCYSK

        BKMFXW()

        CBPHFDX = True
        BHWY = 0
        while BHWY < RJGMHGBC:
            if nums[BHWY] != VPTQSH[BHWY]:
                CBPHFDX = False
                break
            BHWY += 1
        return CBPHFDX