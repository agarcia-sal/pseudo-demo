class Solution:
    def clearStars(self, s: str) -> str:
        def isAsterisk(x: str) -> bool:
            return x == '*'

        def hasElements(lst: list) -> bool:
            return lst != []

        def removeLastElement(lst: list) -> list:
            if lst == []:
                return []
            else:
                return lst[:-1]

        def appendElement(lst: list, el: str) -> list:
            return lst + [el]

        def concatListElements(lst: list) -> str:
            def concatHelper(accum: str, idx: int) -> str:
                if idx >= len(lst):
                    return accum
                else:
                    return concatHelper(accum + lst[idx], idx + 1)
            return concatHelper("", 0)

        def processCharacters(src: str, pos: int, stk: list) -> list:
            if pos >= len(src):
                return stk
            else:
                curChar = src[pos]
                if isAsterisk(curChar):
                    newStack = stk
                    if hasElements(stk):
                        newStack = removeLastElement(stk)
                    return processCharacters(src, pos + 1, newStack)
                else:
                    return processCharacters(src, pos + 1, appendElement(stk, curChar))

        finalStack = processCharacters(s, 0, [])
        return concatListElements(finalStack)