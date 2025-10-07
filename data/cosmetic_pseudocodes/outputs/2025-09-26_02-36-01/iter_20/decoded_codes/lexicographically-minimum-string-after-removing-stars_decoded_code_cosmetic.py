class Solution:
    def clearStars(self, s: str) -> str:
        def deleteLastElement(arr):
            if len(arr) == 0:
                return arr
            else:
                return arr[:-1]

        alpha = []
        omega = 0
        while omega < len(s):
            chi = s[omega:omega+1]
            if chi != "*":
                alpha.append(chi)
            else:
                alpha = deleteLastElement(alpha)
            omega += 1

        def concatenateElements(elements):
            result = ""
            i = 0
            while True:
                if i >= len(elements):
                    break
                result += elements[i]
                i += 1
            return result

        return concatenateElements(alpha)