class Solution:
    def clearStars(self, inputString: str) -> str:
        def deleteLastElement(lst):
            if lst:
                lst.pop()

        buffer = []
        indexVar = 0

        while True:
            if indexVar >= len(inputString):
                break

            currentChar = inputString[indexVar]

            if not (currentChar != '*'):
                deleteLastElement(buffer)
            else:
                buffer.append(currentChar)

            indexVar += 1

        assembledString = ""
        pointer = 0

        while pointer < len(buffer):
            assembledString += buffer[pointer]
            pointer += 1

        return assembledString