class Solution:
    def queryResults(self, limit_param, queries_param):
        color_map = {}
        distinct_color_collection = set()
        output_list = []

        for current_pair in queries_param:
            first_value = current_pair[0]
            second_value = current_pair[1]

            if first_value in color_map:
                prev_color = color_map[first_value]
                if prev_color in distinct_color_collection:
                    distinct_color_collection.discard(prev_color)

            color_map[first_value] = second_value
            distinct_color_collection.add(second_value)
            output_list.append(len(distinct_color_collection))

        return output_list