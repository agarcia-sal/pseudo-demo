class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        kToMod = 10**9 + 7
        arr = [[0] * (x + 1) for _ in range(n + 1)]
        arr[0][0] = 1

        counterA = 1
        while counterA <= n:
            counterB = 1
            while True:
                if counterB > x:
                    break
                prevRowCurrCol = arr[counterA - 1][counterB]
                prevRowPrevCol = arr[counterA - 1][counterB - 1]
                termOne = (prevRowCurrCol * counterB) % kToMod
                termTwo = (prevRowPrevCol * (x - (counterB - 1))) % kToMod
                arr[counterA][counterB] = (termOne + termTwo) % kToMod
                counterB += 1
            counterA += 1

        accumulator = 0
        powerVal = 1
        for idx in range(1, x + 1):
            powerVal = (powerVal * y) % kToMod
            tempVal = (arr[n][idx] * powerVal) % kToMod
            accumulator = (accumulator + tempVal) % kToMod

        return accumulator