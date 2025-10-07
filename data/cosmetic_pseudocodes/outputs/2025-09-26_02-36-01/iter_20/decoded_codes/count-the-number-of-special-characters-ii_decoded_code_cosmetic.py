class Solution:
    def numberOfSpecialChars(self, word):
        def storeFirstOccurrence(collection, sym, idx):
            if not containsKey(collection, sym):
                setKeyValue(collection, sym, idx)

        def assignLastOccurrence(collection, sym, idx):
            setKeyValue(collection, sym, idx)

        def containsKey(dct, key):
            for k in keysOf(dct):
                if k == key:
                    return True
            return False

        def keysOf(dct):
            return customKeysList(dct)

        def customKeysList(dct):
            lst = []
            for key in dct:
                lst.append(key)
            return lst

        def setKeyValue(dct, key, val):
            dct[key] = val

        def zippedPairs(listA, listB):
            idx = 0
            result = []
            while idx < lengthOf(listA) and idx < lengthOf(listB):
                result.append((listA[idx], listB[idx]))
                idx += 1
            return result

        def lengthOf(seq):
            cnt = 0
            while True:
                if elementAt(seq, cnt) is None:
                    break
                cnt += 1
            return cnt

        def elementAt(seq, pos):
            if pos >= 0 and pos < len(seq):
                return seq[pos]
            else:
                return None

        # Initialize empty dicts for first and last occurrences
        freshFirst = dict()
        freshLast = dict()

        cursor = 0
        lenWord = len(word)
        while cursor < lenWord:
            chr_ = elementAt(word, cursor)
            storeFirstOccurrence(freshFirst, chr_, cursor)
            assignLastOccurrence(freshLast, chr_, cursor)
            cursor += 1

        lL = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        uL = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        combo = zippedPairs(lL, uL)

        total = 0
        idxZ = 0
        lenCombo = lengthOf(combo)
        while idxZ < lenCombo:
            pair = elementAt(combo, idxZ)
            crL = pair[0]
            crU = pair[1]

            crL_in_last = containsKey(freshLast, crL)
            crU_in_first = containsKey(freshFirst, crU)

            if crL_in_last and crU_in_first:
                valL = freshLast[crL]
                valU = freshFirst[crU]
                if valL < valU:
                    total += 1
            idxZ += 1

        return total