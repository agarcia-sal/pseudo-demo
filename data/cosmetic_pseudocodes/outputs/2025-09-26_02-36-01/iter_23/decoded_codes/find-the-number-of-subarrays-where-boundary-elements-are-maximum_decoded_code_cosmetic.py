class Solution:
    def numberOfSubarrays(self, nums):
        # CreateDefaultDictionaryList returns a function that provides a defaultdict-like behavior
        def CreateDefaultDictionaryList():
            dict_ = {}

            def access(key):
                if key not in dict_:
                    dict_[key] = []
                return dict_[key]

            return access

        index_map = CreateDefaultDictionaryList()

        # Recursively fill the index_map with indices grouped by value
        def fillMap(i, iter_):
            if not iter_:
                return
            val = iter_[0]
            index_map(val).append(i)
            fillMap(i + 1, iter_[1:])

        fillMap(0, nums)

        totalCount = 0

        # Recursive function to find maximum in a list sub-portion
        def maxInList(lst, idx, currentMax):
            if idx >= len(lst):
                return currentMax
            candidate = lst[idx]
            updatedMax = candidate if candidate > currentMax else currentMax
            return maxInList(lst, idx + 1, updatedMax)

        # Recursive processing of the indices lists per value
        def processIndices(keysList, pos):
            nonlocal totalCount
            if pos >= len(keysList):
                return
            currentIndicesList = index_map(keysList[pos])
            lengthIndices = len(currentIndicesList)

            def outerLoop(a):
                if a >= lengthIndices:
                    return

                def innerLoop(b):
                    if b >= lengthIndices:
                        return
                    startIdx = currentIndicesList[a]
                    endIdx = currentIndicesList[b]
                    subList = nums[startIdx:endIdx + 1]
                    maxVal = maxInList(subList, 0, -1)
                    # Check if maxVal equals nums[startIdx]
                    if maxVal == nums[startIdx]:
                        totalCount += 1
                    innerLoop(b + 1)

                innerLoop(a)
                outerLoop(a + 1)

            outerLoop(0)
            processIndices(keysList, pos + 1)

        allValues = []
        for val in index_map.__closure__[0].cell_contents.keys() if hasattr(index_map, "__closure__") else []:
            allValues.append(val)
        # The above line tries to extract keys from the dict inside the closure.
        # But a simpler approach is to just get keys from the dict itself:
        # However, since index_map is a function closure, we extract its dict.
        # To ensure correctness, rewrite CreateDefaultDictionaryList to return both function and dict

        # We need to fix handling of allValues:
        # Let's change approach: define dict outside access to read keys easily.

        # Re-implement CreateDefaultDictionaryList and index_map with accessible dict
        # To refactor properly:

# Refactor with revised design:

class Solution:
    def numberOfSubarrays(self, nums):
        # CreateDefaultDictionaryList returns a tuple (access_function, underlying_dict)
        def CreateDefaultDictionaryList():
            dict_ = {}

            def access(key):
                if key not in dict_:
                    dict_[key] = []
                return dict_[key]

            return access, dict_

        access, dict_ = CreateDefaultDictionaryList()
        index_map = access

        def fillMap(i, iter_):
            if not iter_:
                return
            val = iter_[0]
            index_map(val).append(i)
            fillMap(i + 1, iter_[1:])

        fillMap(0, nums)

        totalCount = 0

        def maxInList(lst, idx, currentMax):
            if idx >= len(lst):
                return currentMax
            candidate = lst[idx]
            updatedMax = candidate if candidate > currentMax else currentMax
            return maxInList(lst, idx + 1, updatedMax)

        def processIndices(keysList, pos):
            nonlocal totalCount
            if pos >= len(keysList):
                return
            currentIndicesList = index_map(keysList[pos])
            lengthIndices = len(currentIndicesList)

            def outerLoop(a):
                if a >= lengthIndices:
                    return

                def innerLoop(b):
                    if b >= lengthIndices:
                        return
                    startIdx = currentIndicesList[a]
                    endIdx = currentIndicesList[b]
                    subList = nums[startIdx:endIdx + 1]
                    maxVal = maxInList(subList, 0, -1)
                    if maxVal == nums[startIdx]:
                        totalCount += 1
                    innerLoop(b + 1)

                innerLoop(a)
                outerLoop(a + 1)

            outerLoop(0)
            processIndices(keysList, pos + 1)

        allValues = list(dict_.keys())
        processIndices(allValues, 0)
        return totalCount