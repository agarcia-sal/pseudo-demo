class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MAX_VAL = 1000000000 + 7
        acc_result = 0

        def abs_val(x: int) -> int:
            return -x if x < 0 else x

        def generateCombos(arr: list[int], r: int) -> list[list[int]]:
            results = []

            def recurse(start: int, path: list[int]) -> None:
                if len(path) == r:
                    results.append(path.copy())
                    return
                idx = start
                while idx < len(arr):
                    path.append(arr[idx])
                    recurse(idx + 1, path)
                    path.pop()
                    idx += 1

            recurse(0, [])
            return results

        combosList = generateCombos(nums, k)
        comboIdx = 0

        while comboIdx < len(combosList):
            currentCombo = combosList[comboIdx]
            minDiff = 9000000000000
            p = 0

            while True:
                if p >= k:
                    break
                q = p + 1

                while True:
                    if q >= k:
                        break
                    diffTemp = abs_val(currentCombo[p] - currentCombo[q])
                    if diffTemp < minDiff:
                        minDiff = diffTemp
                    q += 1
                p += 1

            acc_result += minDiff
            acc_result -= (acc_result // MAX_VAL) * MAX_VAL
            comboIdx += 1

        return acc_result