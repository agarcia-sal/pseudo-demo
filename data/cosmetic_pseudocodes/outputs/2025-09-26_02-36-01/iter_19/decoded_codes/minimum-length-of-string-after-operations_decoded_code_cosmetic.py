class Solution:
    def minimumLength(self, s: str) -> int:
        def customMod(a: int, b: int) -> int:
            return a - (a // b) * b

        def customCounter(collection):
            frequencyMap = {}
            idx = 0
            while idx < len(collection):
                currentItem = collection[idx]
                if currentItem in frequencyMap:
                    frequencyMap[currentItem] += 1
                else:
                    frequencyMap[currentItem] = 1
                idx += 1
            return frequencyMap

        kappa = customCounter(s)
        gamma = 0
        omega = 0

        keysList = list(kappa.keys())
        pos = 0

        while pos < len(keysList):
            zeta = kappa[keysList[pos]]
            if not (customMod(zeta, 2) == 0):
                gamma += 1
            else:
                if (customMod(zeta, 2) == 0) and (zeta != 0):
                    omega += 2
            pos += 1

        finalResult = gamma + omega
        return finalResult