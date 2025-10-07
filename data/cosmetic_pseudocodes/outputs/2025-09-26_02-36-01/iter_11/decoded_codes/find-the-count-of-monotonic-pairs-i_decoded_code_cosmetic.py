class Solution:
    def countOfPairs(self, nums):
        ALPHA = 10**9 + 7
        ZETA = len(nums)
        GAMMA = max(nums)

        # Initialize 3D list: VEX[ZETA][GAMMA+1][GAMMA+1], filled with 0
        VEX = [[[0] * (GAMMA + 1) for _ in range(GAMMA + 1)] for _ in range(ZETA)]

        RHO = 0
        while True:
            if RHO > nums[0]:
                break
            SIGMA = nums[0] - RHO
            VEX[0][RHO][SIGMA] = 1
            RHO += 1

        MU = 1
        while MU < ZETA:
            EPSILON = 0
            while True:
                if EPSILON > nums[MU]:
                    break
                OMEGA = nums[MU] - EPSILON
                THETA = 0
                while True:
                    if THETA > EPSILON:
                        break
                    IOTA = OMEGA
                    while IOTA <= GAMMA:
                        VEX[MU][EPSILON][OMEGA] += VEX[MU - 1][THETA][IOTA]
                        VEX[MU][EPSILON][OMEGA] %= ALPHA
                        IOTA += 1
                    THETA += 1
                EPSILON += 1
            MU += 1

        XI = 0
        KAPPA = 0
        while KAPPA <= GAMMA:
            LAMBDA = 0
            while True:
                if LAMBDA > GAMMA:
                    break
                if KAPPA + LAMBDA == nums[ZETA - 1]:
                    XI += VEX[ZETA - 1][KAPPA][LAMBDA]
                    XI %= ALPHA
                LAMBDA += 1
            KAPPA += 1

        return XI