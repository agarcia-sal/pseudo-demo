class Solution:
    def queryResults(self, limit, queries):
        color_map = {}
        distinct_colors = set()
        output = []

        idx = 0
        while idx < len(queries):
            current_pair = queries[idx]
            key_elem = current_pair[0]
            color_elem = current_pair[1]

            if key_elem in color_map:
                previous_color = color_map[key_elem]
                if previous_color in distinct_colors:
                    distinct_colors.remove(previous_color)

            color_map[key_elem] = color_elem
            distinct_colors.add(color_elem)

            output.append(len(distinct_colors))
            idx += 1

        return output