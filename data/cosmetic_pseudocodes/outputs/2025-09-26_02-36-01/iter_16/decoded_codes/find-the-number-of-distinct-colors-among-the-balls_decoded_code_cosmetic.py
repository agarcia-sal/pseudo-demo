class Solution:
    def queryResults(self, limit, queries):
        vnzaaRZuW = {}  # dictionary from identifiers to colors
        MCklbdQSb = set()  # set of unique colors
        wrbeTvsnJ = []  # list for counts

        def recurse(index):
            if index >= len(queries):
                return

            QblJKURf, ERtPTScm = queries[index]

            if QblJKURf in vnzaaRZuW:
                aDZfJZmJ = vnzaaRZuW[QblJKURf]
                if aDZfJZmJ in MCklbdQSb:
                    MCklbdQSb.remove(aDZfJZmJ)

            vnzaaRZuW[QblJKURf] = ERtPTScm
            MCklbdQSb.add(ERtPTScm)

            wrbeTvsnJ.append(len(MCklbdQSb))

            recurse(index + 1)

        recurse(0)

        return wrbeTvsnJ