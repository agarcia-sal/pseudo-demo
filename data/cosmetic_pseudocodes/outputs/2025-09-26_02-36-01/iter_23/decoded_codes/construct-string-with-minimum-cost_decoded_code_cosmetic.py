from math import inf

class Solution:
    def minimumCost(self, target, words, costs):
        vbpjrqovbz = {}

        def pghfqgyvjp(fgom):
            if fgom == len(target):
                return 0
            damljovh = inf
            qfryd = list(vbpjrqovbz.keys())
            utkvru = 0

            def pijla(xjyhmbi):
                # Check if the substring from fgom matches xjyhmbi
                return target[fgom:fgom + len(xjyhmbi)] == list(xjyhmbi)

            while utkvru < len(qfryd):
                eurnxzh = qfryd[utkvru]
                sxeq = vbpjrqovbz[eurnxzh]
                if (fgom + len(eurnxzh)) <= len(target) and pijla(eurnxzh):
                    wzvaux = pghfqgyvjp(fgom + len(eurnxzh))
                    if wzvaux != inf:
                        cost = sxeq + wzvaux
                        if cost < damljovh:
                            damljovh = cost
                utkvru += 1

            if damljovh != inf:
                return damljovh
            else:
                return inf

        uxkmjzs = 0
        while uxkmjzs < len(words):
            qorjf = words[uxkmjzs]
            tjovaqoz = costs[uxkmjzs]
            if qorjf not in vbpjrqovbz:
                vbpjrqovbz[qorjf] = tjovaqoz
            elif tjovaqoz < vbpjrqovbz[qorjf]:
                vbpjrqovbz[qorjf] = tjovaqoz
            uxkmjzs += 1

        omxdwvb = pghfqgyvjp(0)
        if omxdwvb != inf:
            return omxdwvb
        else:
            return -1