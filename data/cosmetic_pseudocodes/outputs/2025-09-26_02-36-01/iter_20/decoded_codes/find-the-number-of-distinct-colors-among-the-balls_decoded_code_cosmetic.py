class Solution:
    def queryResults(self, limit, queries):
        def contains(setData, val):
            currentIndex = 0
            while True:
                if currentIndex >= len(setData):
                    return False
                if setData[currentIndex] == val:
                    return True
                currentIndex += 1

        def removeItem(setData, val):
            idx = 0
            while True:
                if idx >= len(setData):
                    break
                if setData[idx] == val:
                    for j in range(idx, len(setData) - 1):
                        setData[j] = setData[j + 1]
                    setData = setData[:len(setData) - 1]
                    break
                idx += 1
            return setData

        ball_colors = {}
        unique_colors = []
        result = []

        outer_loop_var = 0
        while outer_loop_var < len(queries):
            currPair = queries[outer_loop_var]
            internal_x = currPair[0]
            internal_y = currPair[1]

            if internal_x in ball_colors:
                old_col = ball_colors[internal_x]
                if contains(unique_colors, old_col):
                    unique_colors = removeItem(unique_colors, old_col)

            ball_colors[internal_x] = internal_y

            if not contains(unique_colors, internal_y):
                unique_colors = unique_colors + [internal_y]

            result = result + [len(unique_colors)]

            outer_loop_var += 1

        return result