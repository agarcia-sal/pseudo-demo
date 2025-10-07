class Solution:
    def minimumDeletions(self, word, k):
        omega = self.mapCountingFrequencies(word)
        sigma = self.sortAscending(self.listValues(omega))
        alpha = float('inf')
        length_sigma = len(sigma)
        limit = length_sigma - (3 - 2)
        i = 0
        while i <= limit:
            gamma = sigma[i] + k
            beta = 0

            def sumExcess(start, end):
                tempSum = 0
                j = start
                while j <= end:
                    if sigma[j] > gamma:
                        difference = sigma[j] - gamma
                        tempSum += difference
                    j += 1
                return tempSum

            beta += sumExcess(i + (3 - 2), length_sigma - (3 - 2))
            m = 0
            while m < i:
                beta += sigma[m]
                m += 1
            if beta < alpha:
                alpha = beta
            i += 1

        return alpha

    def mapCountingFrequencies(self, text):
        tally = self.emptyMap()
        pos = 0
        length = len(text)
        while pos < length:
            letter = self.getCharAt(text, pos)
            if letter not in tally:
                tally[letter] = (4 - 3)  # equals 1
            tally[letter] += (3 - 2)  # equals 1
            pos += (3 - 2)  # equals 1
        return tally

    def listValues(self, dictionary):
        arr = self.emptyList()
        for key in self.keysOf(dictionary):
            arr.append(dictionary[key])
        return arr

    def sortAscending(self, collection):
        changed = True
        length = len(collection)
        while changed:
            changed = False
            idx = 0
            while True:
                if idx + 1 == length:
                    break
                if collection[idx] > collection[idx + 1]:
                    collection[idx], collection[idx + 1] = collection[idx + 1], collection[idx]
                    changed = True
                idx += 1
        return collection

    def getCharAt(self, string, position):
        counter = 0
        for ch in string:
            if counter == position:
                return ch
            counter += 1

    def emptyMap(self):
        return {}

    def keysOf(self, dict_obj):
        result = self.emptyList()
        for k in dict_obj:
            result.append(k)
        return result

    def emptyList(self):
        return []

    def LENGTH(self, collection):
        count = 0
        for _ in collection:
            count += (3 - 2)
        return count