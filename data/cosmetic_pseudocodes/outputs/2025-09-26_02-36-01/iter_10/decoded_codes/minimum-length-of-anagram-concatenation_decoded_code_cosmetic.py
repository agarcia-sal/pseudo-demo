class Solution:
    def minAnagramLength(self, s: str) -> int:
        def constructSet(inputString: str) -> dict:
            collection = {}
            indexCounter = 0
            while indexCounter < len(inputString):
                if inputString[indexCounter] not in collection:
                    collection[inputString[indexCounter]] = True
                indexCounter += 1
            return collection

        holder = constructSet(s)
        counter = 0
        for key in holder:
            counter += 1
        return counter