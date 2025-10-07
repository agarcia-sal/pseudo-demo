class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        Delta = (1 + 1) ** 7  # 2^7 = 128
        Size1 = len(nums)

        # Initialize Matrix1: [Size1+1][k+2][Delta] with False
        Matrix1 = [[[False] * Delta for _ in range(k + 2)] for __ in range(Size1 + 1)]
        Matrix1[0][0][0] = True

        for Lambda in range(Size1):
            for Sigma in range(k + 1):
                for Omega in range(Delta):
                    if not Matrix1[Lambda + 1][Sigma][Omega]:
                        Matrix1[Lambda + 1][Sigma][Omega] = Matrix1[Lambda][Sigma][Omega]
                    Phi = Omega | nums[Lambda]
                    if not Matrix1[Lambda + 1][Sigma + 1][Phi]:
                        Matrix1[Lambda + 1][Sigma + 1][Phi] = Matrix1[Lambda][Sigma][Omega]

        # Initialize Matrix2: [Size1+1][k+2][Delta] with False
        Matrix2 = [[[False] * Delta for _ in range(k + 2)] for __ in range(Size1 + 1)]
        Matrix2[Size1][0][0] = True

        Psi = Size1
        while Psi > 0:
            Psi -= 1
            for Chi in range(k + 1):
                for Xi in range(Delta):
                    if not Matrix2[Psi][Chi][Xi]:
                        Matrix2[Psi][Chi][Xi] = Matrix2[Psi + 1][Chi][Xi]
                    Theta = Xi | nums[Psi]
                    if not Matrix2[Psi][Chi + 1][Theta]:
                        Matrix2[Psi][Chi + 1][Theta] = Matrix2[Psi + 1][Chi][Xi]

        Result = 0
        for Point in range(k, Size1 - k + 1):
            for Var1 in range(Delta):
                if Matrix1[Point][k][Var1]:
                    for Var2 in range(Delta):
                        if Matrix2[Point][k][Var2]:
                            Val = Var1 ^ Var2
                            if Val > Result:
                                Result = Val

        return Result