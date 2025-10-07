class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # A collection is represented as a list of objects with 'key' and 'value' attributes.
        # We'll define a simple class to hold these pairs to match access patterns.
        class KeyValue:
            __slots__ = ('key', 'value')
            def __init__(self, key, value):
                self.key = key
                self.value = value

        def lookupContainsKey(collection, key):
            index = 0
            while True:
                if index >= len(collection):
                    return False
                if collection[index].key == key:
                    return True
                index += 1

        def assignKeyValue(collection, key, value):
            index = 0
            while True:
                if index >= len(collection):
                    collection.append(KeyValue(key, value))
                    return
                if collection[index].key == key:
                    collection[index].value = value
                    return
                index += 1

        def getValue(collection, key):
            idx = 0
            while idx < len(collection):
                if collection[idx].key == key:
                    return collection[idx].value
                idx += 1

        def getKeys(collection):
            result = []
            idx2 = 0
            while True:
                if idx2 >= len(collection):
                    return result
                result.append(collection[idx2].key)
                idx2 += 1

        LOWERCASE = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        UPPERCASE = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

        first = []  # collection of key-value pairs: first occurrences
        last = []   # collection of key-value pairs: last occurrences

        def processChars(pos, wordlength):
            if pos >= wordlength:
                return
            char = word[pos]
            if not lookupContainsKey(first, char):
                assignKeyValue(first, char, pos)
            assignKeyValue(last, char, pos)
            processChars(pos + 1, wordlength)

        processChars(0, len(word))

        count = 0

        def countAccum(index):
            nonlocal count
            if index >= len(LOWERCASE):
                return count
            a = LOWERCASE[index]
            b = UPPERCASE[index]
            cond1 = lookupContainsKey(last, a)
            cond2 = lookupContainsKey(first, b)
            if cond1 and cond2:
                valA = getValue(last, a)
                valB = getValue(first, b)
                if valA < valB:
                    count += 1
            return countAccum(index + 1)

        return countAccum(0)