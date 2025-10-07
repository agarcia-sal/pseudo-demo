class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 * (10 ** 8) + 1

        def dp(z: int, o: int, last: int, consecutive: int) -> int:
            def isInvalid(a: int) -> bool:
                return a < 0

            def dpInner(z: int, o: int, last: int, consecutive: int, acc: int) -> int:
                if z == 0 and o == 0:
                    return acc
                if isInvalid(z) or isInvalid(o):
                    return 0
                res = 0
                if last == 0:
                    if consecutive < limit:
                        res = (res + dp(z - 1, o, 0, consecutive + 1)) % MOD
                    res = (res + dp(z, o - 1, 1, 1)) % MOD
                else:
                    if z > 0:
                        res = (res + dp(z - 1, o, 0, 1)) % MOD
                    if consecutive < limit:
                        res = (res + dp(z, o - 1, 1, consecutive + 1)) % MOD
                return res

            return dpInner(z, o, last, consecutive, 0)

        def helper(z: int, o: int, last: int, consecutive: int, accum: int) -> int:
            if z == 0 and o == 0:
                return accum % MOD
            if z < 0 or o < 0:
                return accum % MOD
            if last == 0:
                firstBranch = 0
                if consecutive < limit:
                    firstBranch = helper(z - 1, o, 0, consecutive + 1, 0)
                secondBranch = helper(z, o - 1, 1, 1, 0)
                return (accum + firstBranch + secondBranch) % MOD
            else:
                firstBranch = 0
                if z > 0:
                    firstBranch = helper(z - 1, o, 0, 1, 0)
                secondBranch = 0
                if consecutive < limit:
                    secondBranch = helper(z, o - 1, 1, consecutive + 1, 0)
                return (accum + firstBranch + secondBranch) % MOD

        def tailDp(z: int, o: int, last: int, consecutive: int, acc: int) -> int:
            if z == 0 and o == 0:
                return acc % MOD
            if z < 0 or o < 0:
                return acc % MOD
            resultAcc = acc
            if last == 0:
                if consecutive < limit:
                    a = tailDp(z - 1, o, 0, consecutive + 1, 0)
                    resultAcc = (resultAcc + a) % MOD
                b = tailDp(z, o - 1, 1, 1, 0)
                resultAcc = (resultAcc + b) % MOD
            else:
                if z > 0:
                    c = tailDp(z - 1, o, 0, 1, 0)
                    resultAcc = (resultAcc + c) % MOD
                if consecutive < limit:
                    d = tailDp(z, o - 1, 1, consecutive + 1, 0)
                    resultAcc = (resultAcc + d) % MOD
            return resultAcc

        functionStack = [(zero, one - 1, 0, 0, 1)]

        def recursiveWrapper(z: int, o: int, last: int, consecutive: int) -> int:
            if z == 0 and o == 0:
                return 1
            if z < 0 or o < 0:
                return 0
            sumTotal = 0
            if last == 0:
                if consecutive < limit:
                    sumTotal = (sumTotal + recursiveWrapper(z - 1, o, 0, consecutive + 1)) % MOD
                sumTotal = (sumTotal + recursiveWrapper(z, o - 1, 1, 1)) % MOD
            else:
                if z > 0:
                    sumTotal = (sumTotal + recursiveWrapper(z - 1, o, 0, 1)) % MOD
                if consecutive < limit:
                    sumTotal = (sumTotal + recursiveWrapper(z, o - 1, 1, consecutive + 1)) % MOD
            return sumTotal % MOD

        def iterativeDp(z: int, o: int, last: int, consecutive: int) -> int:
            stack = [(z, o, last, consecutive)]
            memo = {}
            while stack:
                current = stack.pop()
                cz, co, clast, cconsecutive = current
                if (cz, co, clast, cconsecutive) in memo:
                    continue
                if cz == 0 and co == 0:
                    memo[(cz, co, clast, cconsecutive)] = 1
                    continue
                if cz < 0 or co < 0:
                    memo[(cz, co, clast, cconsecutive)] = 0
                    continue
                val = 0
                pending = []
                if clast == 0:
                    if cconsecutive < limit:
                        pending.append((cz - 1, co, 0, cconsecutive + 1))
                    pending.append((cz, co - 1, 1, 1))
                else:
                    if cz > 0:
                        pending.append((cz - 1, co, 0, 1))
                    if cconsecutive < limit:
                        pending.append((cz, co - 1, 1, cconsecutive + 1))
                allComputed = True
                for p in pending:
                    if p not in memo:
                        stack.append(current)
                        stack.append(p)
                        allComputed = False
                        break
                if allComputed:
                    for p in pending:
                        val = (val + memo[p]) % MOD
                    memo[(cz, co, clast, cconsecutive)] = val
            return memo[(z, o, last, consecutive)]

        # The problem's main return is from dp with arguments (zero, one - 1, 0, 0)
        return dp(zero, one - 1, 0, 0)