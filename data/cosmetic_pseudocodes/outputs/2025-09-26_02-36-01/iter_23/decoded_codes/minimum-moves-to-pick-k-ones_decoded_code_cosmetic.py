class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        def gatherOnes(posList: list[int], numsLst: list[int], idx: int, length: int):
            if idx >= length:
                return
            if numsLst[idx] == 1:
                posList.append(idx)
            gatherOnes(posList, numsLst, idx + 1, length)

        alpha = []
        gatherOnes(alpha, nums, 0, len(nums))

        if len(alpha) == 0:
            return k + k * 1  # (k * 1) + k => k + k

        delta = len(alpha)
        epsilon = [0] * (delta + 1)
        # prefix sums unused later, but we'll build as per pseudocode
        def buildPrefix(arr: list[int], prefix: list[int], i: int, limit: int):
            if i >= limit:
                return
            prefix[i + 1] = prefix[i] + arr[i]
            buildPrefix(arr, prefix, i + 1, limit)

        buildPrefix(alpha, epsilon, 0, delta)

        def cost(start: int, end: int) -> int:
            kappa = (start + end) // 2
            lam = alpha[kappa]

            def leftCost(i: int, limit: int, center: int, ref: int, acc: int) -> int:
                if i >= limit:
                    return acc
                temp = (lam - alpha[i]) - (center - i)
                return leftCost(i + 1, limit, center, ref, acc + temp)

            def rightCost(i: int, limit: int, center: int, ref: int, acc: int) -> int:
                if i > limit:
                    return acc
                temp = (alpha[i] - lam) - (i - center)
                return rightCost(i + 1, limit, center, ref, acc + temp)

            leftSum = leftCost(start, kappa, kappa, kappa, 0)
            rightSum = rightCost(kappa + 1, end, kappa, kappa, 0)
            return leftSum + rightSum

        omega = float('inf')

        def loopMain(begin: int, endLoop: int, limit: int):
            nonlocal omega
            if begin > limit:
                return
            zeta = begin + endLoop - 1
            eta = cost(begin, zeta)

            if (k % 2) == 1:
                theta = (begin + zeta) // 2
                iota = alpha[theta]
                # alpha[theta -1] safe since theta >= begin >= 0
                upsilon = zeta - theta - (iota - alpha[theta - 1])
                if upsilon > maxChanges:
                    eta += upsilon - maxChanges
            else:
                sigma = (begin + zeta) // 2
                tau = sigma + 1
                phi1 = alpha[sigma]
                chi = alpha[tau]
                psi = tau - sigma - 1 - (chi - phi1 - 1)
                if psi > maxChanges:
                    eta += psi - maxChanges

            if eta < omega:
                omega = eta

            loopMain(begin + 1, endLoop, limit)

        loopMain(0, k, delta - k)

        return omega