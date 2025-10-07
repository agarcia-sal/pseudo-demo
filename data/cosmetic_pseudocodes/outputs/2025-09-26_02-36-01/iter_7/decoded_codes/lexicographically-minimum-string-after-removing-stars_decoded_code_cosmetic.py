class Solution:
    def clearStars(self, inputString: str) -> str:
        container = []
        indexCounter = 0

        while indexCounter < len(inputString):
            if inputString[indexCounter] != "*":
                container.append(inputString[indexCounter])
            elif len(container) > 0:
                container.pop()
            indexCounter += 1

        combinedResult = ""
        position = 0

        while position < len(container):
            combinedResult += container[position]
            position += 1

        return combinedResult