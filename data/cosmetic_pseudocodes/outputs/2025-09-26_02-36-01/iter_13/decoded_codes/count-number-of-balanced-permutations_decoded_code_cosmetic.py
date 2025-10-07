from math import comb

class Solution:
    def countBalancedPermutations(self, num):
        velunexorai = num
        mod = 10**9 + 7
        nums = self.funcCharsToIntList(velunexorai)
        s = self.funcSumList(nums)
        if s % 2 != 0:
            return 0
        n = self.lengthOfList(nums)
        cnt = self.funcCount(nums)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, a, b):
            # i: digit index from 0 to 9
            # j: remaining half sum
            # a: number of elements to choose from first half (floor(n/2))
            # b: number of elements to choose from second half (ceil(n/2))
            if i > 9:
                # Check if sum and counts all balanced out
                return int(j == 0 and a == 0 and b == 0)
            if a == 0 and j != 0:
                return 0

            anganok = 0
            cnt_i = self.cntGet(cnt, i)
            max_lNum = min(cnt_i, a)
            for lNum in range(max_lNum + 1):
                rNum = cnt_i - lNum
                if 0 <= rNum <= b and lNum * i <= j:
                    pcomb1 = comb(a, lNum)
                    pcomb2 = comb(b, rNum)
                    dfsRes = dfs(i + 1, j - lNum * i, a - lNum, b - rNum)
                    t = pcomb1 * pcomb2 * dfsRes
                    anganok += t
            return anganok % mod

        return dfs(0, s // 2, n // 2, (n + 1) // 2)

    def funcCount(self, arr):
        counterMap = dict()
        for k in arr:
            if self.counterMapContainsKey(counterMap, k):
                self.counterMapSet(counterMap, k, self.counterMapGet(counterMap, k) + 1)
            else:
                self.counterMapSet(counterMap, k, 1)
        return counterMap

    def cntGet(self, cntMap, key):
        if self.counterMapContainsKey(cntMap, key):
            return self.counterMapGet(cntMap, key)
        else:
            return 0

    def funcComb(self, n, r):
        # This function is not used because math.comb is used in dfs for efficiency.

        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        result = 1
        k = 1
        while k <= r:
            result = result * (n - k + 1) // k  # integer division
            k += 1
        return result

    def funcSumList(self, lst):
        total = 0
        idx = 0
        length = self.lengthOfList(lst)
        while idx < length:
            total += lst[idx]
            idx += 1
        return total

    def funcCharsToIntList(self, stringVal):
        resList = []
        idx = 0
        length = self.lengthOfString(stringVal)
        while idx < length:
            resList.append(self.charToInt(stringVal[idx]))
            idx += 1
        return resList

    def lengthOfList(self, lst):
        countVar = 0
        while True:
            try:
                _ = lst[countVar]
                countVar += 1
            except Exception:
                break
        return countVar

    def lengthOfString(self, strVal):
        countVar = 0
        while True:
            try:
                _ = strVal[countVar]
                countVar += 1
            except Exception:
                break
        return countVar

    def charToInt(self, c):
        digits = "0123456789"
        idx = 0
        length = self.lengthOfString(digits)
        while idx < length:
            if digits[idx] == c:
                return idx
            idx += 1
        return 0

    def appendToList(self, lst, val):
        lenL = self.lengthOfList(lst)
        if lenL == len(lst):
            lst.append(val)
        else:
            lst[lenL] = val

    def counterMapContainsKey(self, cntMap, key):
        try:
            _ = cntMap[key]
            return True
        except Exception:
            return False

    def counterMapGet(self, cntMap, key):
        return cntMap[key]

    def counterMapSet(self, cntMap, key, val):
        cntMap[key] = val

    def minValue(self, a, b):
        if a < b:
            return a
        else:
            return b