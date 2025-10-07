class Solution:
    def numberOfWays(self, n: int) -> int:
        x = 10**9 + 7

        def moduloAdd(a: int, b: int, m: int) -> int:
            return ((a % m) + (b % m)) % m

        def iterateCoins(cList: list[int], lengthN: int, accArray: list[int]) -> list[int]:
            if not cList:
                return accArray
            else:
                currentCoin = cList[0]
                tailCoins = cList[1:]

                def updateArray(idx: int, arr: list[int]) -> list[int]:
                    if idx > lengthN:
                        return arr
                    newVal = moduloAdd(arr[idx], arr[idx - currentCoin], x)
                    arr[idx] = newVal
                    return updateArray(idx + 1, arr)

                updatedArr = updateArray(currentCoin, accArray)
                return iterateCoins(tailCoins, lengthN, updatedArr)

        def accResult(maxN: int, dpArr: list[int], loopK: int, accum: int) -> int:
            if loopK > 2:
                return accum
            else:
                productVal = loopK * 4
                if productVal <= maxN:
                    newAccum = moduloAdd(accum, dpArr[maxN - productVal], x)
                    return accResult(maxN, dpArr, loopK + 1, newAccum)
                else:
                    return accResult(maxN, dpArr, loopK + 1, accum)

        VwqtrbXhYOIj = [0] * (n + 1)
        VwqtrbXhYOIj[0] = 1

        MpcedFNLbe = iterateCoins([1, 2, 6], n, VwqtrbXhYOIj)
        RmDveYWJkH = accResult(n, MpcedFNLbe, 0, 0)
        return RmDveYWJkH