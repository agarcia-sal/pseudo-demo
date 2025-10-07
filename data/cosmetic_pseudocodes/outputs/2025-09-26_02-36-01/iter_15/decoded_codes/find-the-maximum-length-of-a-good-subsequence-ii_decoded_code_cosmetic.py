from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        D = len(nums)
        M = k + 1
        A = [[0] * M for _ in range(D)]
        B = [defaultdict(int) for _ in range(M)]
        C = [[0, 0, 0] for _ in range(M)]
        R = 0

        for J in range(D):
            Z = nums[J]
            for I in range(M):
                E = B[I][Z]
                A[J][I] = E
                if I > 0:
                    if C[I][0] != Z:
                        A[J][I] = max(A[J][I], C[I][1])
                    else:
                        A[J][I] = max(A[J][I], C[I][2])
                A[J][I] += 1
                B[I][Z] = max(B[I][Z], A[J][I])
                if C[I][0] != Z:
                    if A[J][I] >= C[I][1]:
                        C[I][2] = C[I][1]
                        C[I][1] = A[J][I]
                        C[I][0] = Z
                    else:
                        C[I][2] = max(C[I][2], A[J][I])
                else:
                    C[I][1] = max(C[I][1], A[J][I])
                R = max(R, A[J][I])

        return R