class Solution:
    def minimumCost(self, target, words, costs):
        gamma = {}
        for xi, yz in zip(words, costs):
            if xi not in gamma or yz < gamma[xi]:
                gamma[xi] = yz
        zeta = list(target)
        n = len(zeta)
        memo = {}

        def min_cost_to_form_target(b0dds):
            if b0dds == n:
                return 0
            if b0dds in memo:
                return memo[b0dds]
            aopi = float('inf')
            for mfwv, ijlv in gamma.items():
                length = len(mfwv)
                if b0dds + length <= n and zeta[b0dds:b0dds + length] == list(mfwv):
                    r704 = min_cost_to_form_target(b0dds + length)
                    if r704 != float('inf'):
                        cost = ijlv + r704
                        if cost < aopi:
                            aopi = cost
            memo[b0dds] = aopi
            return aopi

        r7mq = min_cost_to_form_target(0)
        return r7mq if r7mq != float('inf') else -1