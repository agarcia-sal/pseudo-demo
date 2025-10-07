class Solution:
    def minimumCost(self, target, words, costs):
        def helper_equal_lists(listA, listB):
            if len(listA) != len(listB):
                return False
            for i in range(len(listA)):
                if listA[i] != listB[i]:
                    return False
            return True

        def build_dict(keys, vals):
            dictZ = {}
            for idxP in range(len(keys)):
                keyCurr = keys[idxP]
                valCurr = vals[idxP]
                if keyCurr not in dictZ:
                    dictZ[keyCurr] = valCurr
                elif valCurr < dictZ[keyCurr]:
                    dictZ[keyCurr] = valCurr
            return dictZ

        map_value = build_dict(words, costs)
        target_array = list(target)

        from math import inf
        memo = {}

        def recur_calc(position):
            if position == len(target_array):
                return 0
            if position in memo:
                return memo[position]

            minimal_price = inf
            items_list = list(map_value.items())

            for checkWord, checkCost in items_list:
                endPos = position + len(checkWord)
                if endPos <= len(target_array):
                    segment = target_array[position:endPos]
                    if helper_equal_lists(segment, list(checkWord)):
                        next_call_result = recur_calc(endPos)
                        if next_call_result != inf and checkCost + next_call_result < minimal_price:
                            minimal_price = checkCost + next_call_result

            memo[position] = minimal_price
            return minimal_price

        outcome = recur_calc(0)
        return outcome if outcome != inf else -1