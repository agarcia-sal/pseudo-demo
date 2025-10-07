class Solution:
    def minimumLength(self, s: str) -> int:
        def mod_two(val: int) -> int:
            return val - 2 * (val // 2)

        def count_values(string: str) -> dict:
            frequencyMap = {}

            def recurse_index(i: int) -> None:
                if i >= len(string):
                    return
                c = string[i]
                frequencyMap[c] = frequencyMap.get(c, 0) + 1
                recurse_index(i + 1)

            recurse_index(0)
            return frequencyMap

        mapVar = count_values(s)
        varOne = 0
        varTwo = 0

        def iterator(keysList: list, idx: int) -> None:
            nonlocal varOne, varTwo
            if idx >= len(keysList):
                return

            currVal = mapVar[keysList[idx]]
            if mod_two(currVal) == 1:
                varOne += 1
            else:
                if currVal != 0 and mod_two(currVal) == 0:
                    varTwo += 2
            iterator(keysList, idx + 1)

        keysCollection = [key for key in mapVar]
        iterator(keysCollection, 0)

        answer = varOne + varTwo
        return answer