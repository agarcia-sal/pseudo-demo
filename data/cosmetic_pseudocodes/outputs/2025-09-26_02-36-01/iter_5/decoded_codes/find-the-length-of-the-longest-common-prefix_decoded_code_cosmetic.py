class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        def buildPrefixes(index, seq, prefxs):
            if index >= len(seq):
                return prefxs
            stringForm = str(seq[index])

            def collectSubprefixes(pos, endPos):
                if pos > endPos:
                    return
                prefixFragment = stringForm[:pos]
                prefxs.add(prefixFragment)
                collectSubprefixes(pos + 1, endPos)

            collectSubprefixes(1, len(stringForm))
            return buildPrefixes(index + 1, seq, prefxs)

        prefixesSet1 = set()
        prefixesSet1 = buildPrefixes(0, arr1, prefixesSet1)

        def buildPrefixes2(index, seq, prefxs):
            if index >= len(seq):
                return prefxs
            stringForm2 = str(seq[index])

            def collectSubprefixes2(pos2, endPos2):
                if pos2 > endPos2:
                    return
                prefixFragment2 = stringForm2[:pos2]
                prefxs.add(prefixFragment2)
                collectSubprefixes2(pos2 + 1, endPos2)

            collectSubprefixes2(1, len(stringForm2))
            return buildPrefixes2(index + 1, seq, prefxs)

        prefixesSet2 = set()
        prefixesSet2 = buildPrefixes2(0, arr2, prefixesSet2)

        maxLength = 0

        prefixList = list(prefixesSet1)

        def checkPrefixes(iter_):
            nonlocal maxLength
            if iter_ == len(prefixList):
                return
            element = prefixList[iter_]
            if element in prefixesSet2:
                if len(element) > maxLength:
                    maxLength = len(element)
            checkPrefixes(iter_ + 1)

        checkPrefixes(0)

        return maxLength