class Solution:
    def numberOfWays(self, n: int) -> int:
        CONST_MODULO = 10**9 + 7
        dpList = [0] * (n + 1)
        dpList[0] = 1

        def iterateCoins(index: int):
            if index >= 3:
                return
            coinValue = 1 if index == 0 else 2 if index == 1 else 6

            def recursiveLoop(counter: int):
                if counter > n:
                    return
                additionValue = dpList[counter - coinValue]
                previousValue = dpList[counter]
                updatedValue = previousValue + additionValue
                # modulo optimization to avoid large numbers
                dpList[counter] = updatedValue if updatedValue < CONST_MODULO else updatedValue - CONST_MODULO
                recursiveLoop(counter + 1)

            recursiveLoop(coinValue)
            iterateCoins(index + 1)

        iterateCoins(0)

        sumResult = 0
        loopIndex = 0
        while True:
            if (loopIndex * 4) > n:
                break
            tempIndex = n - (loopIndex * 4)
            tempSum = sumResult + dpList[tempIndex]
            sumResult = tempSum if tempSum < CONST_MODULO else tempSum - CONST_MODULO
            loopIndex += 1

        return sumResult