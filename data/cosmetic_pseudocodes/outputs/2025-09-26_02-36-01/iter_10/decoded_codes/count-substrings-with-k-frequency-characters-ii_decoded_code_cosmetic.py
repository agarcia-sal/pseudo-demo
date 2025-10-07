class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def countMapIncrement(m: dict, key: str) -> None:
            if key not in m:
                m[key] = 1
            else:
                m[key] += 1

        def countMapDecrement(m: dict, key: str) -> None:
            m[key] -= 1
            if m[key] == 0:
                del m[key]

        def hasAnyKeyWithCountGE(m: dict, threshold: int) -> bool:
            def helper(keys: list, index: int) -> bool:
                if index >= len(keys):
                    return False
                else:
                    if m[keys[index]] >= threshold:
                        return True
                    else:
                        return helper(keys, index + 1)
            return helper(list(m.keys()), 0)

        alphaPos = 0
        accumAns = 0
        counter = {}
        rightIndex = 0

        def loopRight(index: int) -> None:
            nonlocal alphaPos, accumAns
            if index == len(s):
                return
            else:
                charAtRight = s[index]
                countMapIncrement(counter, charAtRight)

                def contractLeft():
                    nonlocal alphaPos
                    if hasAnyKeyWithCountGE(counter, k):
                        charAtLeft = s[alphaPos]
                        countMapDecrement(counter, charAtLeft)
                        alphaPos += 1
                        contractLeft()
                contractLeft()
                accumAns += alphaPos
                loopRight(index + 1)

        loopRight(0)
        return accumAns