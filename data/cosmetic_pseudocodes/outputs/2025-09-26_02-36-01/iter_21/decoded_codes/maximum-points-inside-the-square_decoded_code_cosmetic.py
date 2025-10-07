class Solution:
    def maxPointsInsideSquare(self, s):
        l = len(s)
        r = 0

        def insideSquare(a):
            return -a if a < 0 else a

        def maxVal(m, n):
            return m if m > n else n

        def containsAllUnique(m):
            dictionary_temp = {}
            flag_valid = True
            index_k = 0

            while index_k < l and flag_valid:
                val_x, val_y = s[index_k]
                if insideSquare(val_x) <= m:
                    if insideSquare(val_y) <= m:
                        tag_c = s[index_k]
                        if tag_c in dictionary_temp:
                            flag_valid = False
                        else:
                            dictionary_temp[tag_c] = True
                index_k += 1

            return flag_valid, len(dictionary_temp)

        counter_i = 0
        while counter_i < l:
            coord_x, coord_y = s[counter_i]
            side = maxVal(insideSquare(coord_x), insideSquare(coord_y))
            is_valid, count_tags = containsAllUnique(side)
            if is_valid and count_tags > r:
                r = count_tags
            counter_i += 1

        return r