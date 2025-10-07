class Solution:
    def queryResults(self, limit, queries):
        empty_mapping = {}
        distinct_collection = set()
        output_sequence = []
        index_tracker = 0

        while index_tracker < limit:
            current_pair = queries[index_tracker]
            x_param = current_pair[0]
            y_param = current_pair[1]

            if x_param in empty_mapping:
                prior_color = empty_mapping[x_param]
                if prior_color in distinct_collection:
                    distinct_collection.remove(prior_color)

            empty_mapping[x_param] = y_param
            distinct_collection.add(y_param)
            output_sequence.append(len(distinct_collection))
            index_tracker += 1

        return output_sequence