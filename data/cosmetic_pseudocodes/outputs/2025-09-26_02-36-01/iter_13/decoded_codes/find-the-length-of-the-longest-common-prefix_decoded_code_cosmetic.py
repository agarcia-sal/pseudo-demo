class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        def toString(number):
            if number == 0:
                return '0'
            digits = []
            temp = number
            while temp > 0:
                remainder = temp % 10
                digits.insert(0, chr(remainder + 48))
                temp //= 10
            return ''.join(digits)

        def insertPrefixes(number_str, prefix_collection):
            length_val = len(number_str)

            def addPrefixesRec(pos):
                if pos > length_val:
                    return
                current_substr = ""
                i = 1
                while i <= pos:
                    current_substr += number_str[i - 1]
                    i += 1
                prefix_collection.add(current_substr)
                addPrefixesRec(pos + 1)

            addPrefixesRec(1)

        prefixes1 = set()

        def processArr1(index):
            if index > len(arr1):
                return
            num_str = toString(arr1[index - 1])
            insertPrefixes(num_str, prefixes1)
            processArr1(index + 1)

        processArr1(1)

        prefixes2 = set()
        idx_tracker = 1
        while idx_tracker <= len(arr2):
            num_str = toString(arr2[idx_tracker - 1])
            insertPrefixes(num_str, prefixes2)
            idx_tracker += 1

        max_common_len = 0

        def checkPrefixes(iterator):
            nonlocal max_common_len
            iterator_list = list(iterator)

            def innerCheck(pos):
                if pos > len(iterator_list):
                    return
                element = iterator_list[pos - 1]
                if element in prefixes2 and len(element) > max_common_len:
                    max_common_len = len(element)
                innerCheck(pos + 1)

            innerCheck(1)

        checkPrefixes(prefixes1)

        return max_common_len