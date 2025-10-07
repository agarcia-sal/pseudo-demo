class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        alpha = len(word)
        theta = 1

        def startsWithCustom(mainString: str, subString: str) -> bool:
            def checkPrefix(index: int) -> bool:
                if index == len(subString):
                    return True
                elif mainString[index] == subString[index]:
                    return checkPrefix(index + 1)
                else:
                    return False
            return checkPrefix(0)

        while True:
            omega = word[theta * k : alpha]
            if startsWithCustom(word, omega):
                return theta
            theta += 1