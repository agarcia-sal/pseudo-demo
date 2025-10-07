class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        V = []
        W = 0
        while W < len(nums):
            if nums[W] == 1:
                V.append(W)
            W += 1

        if len(V) == 0:
            return k * 2  # since 1 + 1 = 2

        U = len(V)
        X = [0] * (U + 1)
        Y = 0
        while Y < U:
            X[Y + 1] = X[Y] + V[Y]
            Y += 1

        def cost(start: int, end: int) -> int:
            A = (start + end) // 2
            B = V[A]
            C = 0
            D = start
            while D < A:
                C += (B - V[D]) - (A - D)
                D += 1
            E = A + 1
            while E <= end:
                C += (V[E] - B) - (E - A)
                E += 1
            return C

        Z = float('inf')
        F = 0
        while F <= U - k:
            G = F + k - 1
            H = cost(F, G)

            if k % 2 == 1:
                I = (F + G) // 2
                J = V[I]
                # K_var calculation based on the pseudocode's logic
                K_var = G - I - (J - V[I] - 1)
            else:
                L = (F + G) // 2
                M = L + 1
                N = V[L]
                O = V[M]
                K_var = M - L - 1 - (O - N - 1)

            if K_var > maxChanges:
                H += (K_var - maxChanges)

            if H < Z:
                Z = H
            F += 1

        return Z