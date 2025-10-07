class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        def convertToInt(strval: str) -> int:
            result = 0
            for ch in strval:
                result = result * 10 + (ord(ch) - ord('0'))
            return result

        def decrementByOne(val_holder: list) -> None:
            val_holder[0] += -1

        def strRepeat(ch: str, count: int) -> str:
            return ch * count

        if n == 1:
            z = 9
            while z >= 1:
                if z % k == 0:
                    return str(z)
                z -= 1
            return "0"

        m = (n + 1) // 2
        nineString = strRepeat('9', m)
        halfValue_holder = [convertToInt(nineString)]

        def strReverse(s: str) -> str:
            return s[::-1]

        while halfValue_holder[0] > 0:
            halfStr = str(halfValue_holder[0])
            reversedStr = strReverse(halfStr)
            if n % 2 == 0:
                combined = halfStr + reversedStr
            else:
                truncated = halfStr[:-1]
                combined = halfStr + strReverse(truncated)

            combinedInt = convertToInt(combined)
            if combinedInt % k == 0:
                return combined

            decrementByOne(halfValue_holder)

        return "0"