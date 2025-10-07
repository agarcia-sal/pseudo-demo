class Solution:
    def countOfPairs(self, dataList):
        BASE_MOD = 1_000_000_000 + 7
        totalCount = len(dataList)
        highestValue = max(dataList)

        # table[current_index][jVal][kVal] stores counts modulo BASE_MOD
        table = [
            [[0] * (highestValue + 1) for _ in range(highestValue + 1)]
            for _ in range(totalCount)
        ]

        def InitializeRow(index):
            def helperLoop(value):
                if value > dataList[0]:
                    return
                complement = dataList[0] - value
                table[index][value][complement] = 1
                helperLoop(value + 1)
            helperLoop(0)

        InitializeRow(0)

        def processIndex(current):
            if current >= totalCount:
                return

            val = dataList[current]

            def outerLoop(jVal):
                if jVal > val:
                    return
                kVal = val - jVal

                def middleLoop(jPrev):
                    if jPrev > jVal:
                        return

                    def innerLoop(kPrev):
                        if kPrev > highestValue:
                            return

                        prev_val = table[current - 1][jPrev][kPrev]
                        if prev_val:
                            table[current][jVal][kVal] = (table[current][jVal][kVal] + prev_val) % BASE_MOD
                        innerLoop(kPrev + 1)

                    innerLoop(0)
                    middleLoop(jPrev + 1)

                middleLoop(0)
                outerLoop(jVal + 1)

            outerLoop(0)
            processIndex(current + 1)

        processIndex(1)

        accumulator = 0

        def sumJudgments(xPos):
            nonlocal accumulator
            if xPos > highestValue:
                return

            def sumK(kPos):
                nonlocal accumulator
                if kPos > highestValue:
                    return
                if xPos + kPos == dataList[-1]:
                    accumulator = (accumulator + table[totalCount - 1][xPos][kPos]) % BASE_MOD
                sumK(kPos + 1)

            sumK(0)
            sumJudgments(xPos + 1)

        sumJudgments(0)

        return accumulator