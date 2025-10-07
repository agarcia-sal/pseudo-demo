class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        def containsKey(coll, key):
            for k in coll:
                if k == key:
                    return True
            return False

        def getValue(coll, key):
            for k, v in coll:
                if k == key:
                    return v
            return None

        def setValue(coll, key, val):
            index = 0
            while index < len(coll):
                k, _ = coll[index]
                if k == key:
                    coll[index] = (k, val)
                    return
                index += 1
            coll.append((key, val))

        def zipCollections(c1, c2):
            result = []
            i = 0
            while i < len(c1) and i < len(c2):
                result.append((c1[i], c2[i]))
                i += 1
            return result

        lowerLetters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        upperLetters = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

        firstMap = []
        lastMap = []

        def processIndex(i):
            if i >= len(word):
                return
            c = word[i]
            if not containsKey(firstMap, c):
                setValue(firstMap, c, i)
            setValue(lastMap, c, i)
            processIndex(i + 1)

        processIndex(0)

        total = 0
        INDEX = 0
        while True:
            if INDEX >= len(lowerLetters) or INDEX >= len(upperLetters):
                break
            lch = lowerLetters[INDEX]
            uch = upperLetters[INDEX]
            if containsKey(lastMap, lch):
                if containsKey(firstMap, uch):
                    lval = getValue(lastMap, lch)
                    uval = getValue(firstMap, uch)
                    if lval < uval:
                        total += 1
            INDEX += 1

        return total