class Solution:
    def numberOfSubarrays(self, nums):
        def max_value(arr, start_idx, end_idx):
            acc = arr[start_idx]
            k = start_idx + 1
            while k <= end_idx:
                if arr[k] > acc:
                    acc = arr[k]
                k += 1
            return acc

        def map_get_or_create(map_ref, key):
            if key not in map_ref:
                map_ref[key] = []
            return map_ref[key]

        dict_indexMap = {}

        outer_counter = 0
        while True:
            if outer_counter >= len(nums):
                break
            element = nums[outer_counter]
            list_ref = map_get_or_create(dict_indexMap, element)
            list_ref.append(outer_counter)
            outer_counter += 1

        result_count = 0
        all_indices_lists = []
        for key in dict_indexMap:
            all_indices_lists.append(dict_indexMap[key])

        outerListPointer = 0
        while outerListPointer < len(all_indices_lists):
            currentList = all_indices_lists[outerListPointer]
            lenList = 0
            while True:
                if lenList >= len(currentList):
                    break
                inner0 = lenList

                inner1 = inner0
                while inner1 < len(currentList):
                    startPos = currentList[inner0]
                    endPos = currentList[inner1]

                    subArr = []
                    idxCopy = startPos
                    while idxCopy <= endPos:
                        subArr.append(nums[idxCopy])
                        idxCopy += 1

                    maxVal = max_value(subArr, 0, len(subArr) - 1)
                    if not (maxVal != nums[startPos]):
                        result_count += 1
                    inner1 += 1

                lenList += 1

            outerListPointer += 1

        return result_count