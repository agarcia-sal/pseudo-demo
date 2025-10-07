class Solution:
    def countMatchingSubarrays(self, alist, bpattern):
        def determine_relation(xval, yval):
            if not (xval >= yval):
                return 1
            elif xval == yval:
                return 0
            else:
                return -1

        length_a = len(alist)
        length_b = len(bpattern)
        total_matches = 0

        rels = []
        pos = 0
        while pos < length_a - 1:
            relation_result = determine_relation(alist[pos], alist[pos + 1])
            rels.append(relation_result)
            pos += 1

        def check_match(idx, limit, relarray, pat):
            if idx >= limit:
                return 0
            else:
                slice_sublist = relarray[idx : idx + length_b]
                matches_here = 0
                if slice_sublist == pat:
                    matches_here += 1
                return matches_here + check_match(idx + 1, limit, relarray, pat)

        search_limit = length_a - length_b
        result_count = check_match(0, search_limit, rels, bpattern)

        return result_count