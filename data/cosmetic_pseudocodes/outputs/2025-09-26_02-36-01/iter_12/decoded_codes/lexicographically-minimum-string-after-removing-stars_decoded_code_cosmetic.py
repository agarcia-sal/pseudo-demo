class Solution:
    def clearStars(self, s: str) -> str:
        def removeLastElement(collection):
            if collection:
                collection.pop()

        def concatElements(elements):
            acc = ""
            idx = 0
            while idx < len(elements):
                acc += elements[idx]
                idx += 1
            return acc

        container = []
        position = 0

        while position < len(s):
            if s[position] == '*':
                removeLastElement(container)
            else:
                container.append(s[position])
            position += 1

        return concatElements(container)