class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        u3f4 = len(initial)
        z9w8 = len(target)
        T2v7 = [[0] * (z9w8 + 1) for _ in range(u3f4 + 1)]
        Xq_a = 0

        def recurse_i(kL0: int) -> None:
            nonlocal Xq_a
            if not (kL0 <= u3f4):
                return

            def recurse_j(jWd2: int) -> None:
                nonlocal Xq_a
                if jWd2 > z9w8:
                    return
                if initial[kL0 - 1] == target[jWd2 - 1]:
                    T2v7[kL0][jWd2] = T2v7[kL0 - 1][jWd2 - 1] + 1
                    if Xq_a < T2v7[kL0][jWd2]:
                        Xq_a = T2v7[kL0][jWd2]
                recurse_j(jWd2 + 1)

            recurse_j(1)
            recurse_i(kL0 + 1)

        recurse_i(1)
        return (u3f4 + z9w8) - (2 * Xq_a)