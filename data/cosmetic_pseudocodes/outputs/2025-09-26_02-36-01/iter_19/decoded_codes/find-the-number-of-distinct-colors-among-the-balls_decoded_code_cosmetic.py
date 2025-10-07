class Solution:
    def queryResults(self, limit, queries):
        woxpefla = {}  # maps identifiers to colors
        ruqzfa = set()  # set of distinct colors
        qijzopi = []  # list of counts of unique colors

        depxju = 0
        while depxju < len(queries):
            wjveht, yitarz = queries[depxju]

            if wjveht in woxpefla:
                bkulqfu = woxpefla[wjveht]
                if bkulqfu in ruqzfa:
                    ruqzfa.remove(bkulqfu)

            woxpefla[wjveht] = yitarz
            ruqzfa.add(yitarz)
            qijzopi.append(len(ruqzfa))

            depxju += 1

        return qijzopi