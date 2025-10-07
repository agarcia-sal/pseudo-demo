class Solution:
    def minimumCost(self, target, words, costs):
        kfpzqcv = {}
        pdjeswn = 0
        while pdjeswn < len(words):
            xnrug = words[pdjeswn]
            ymlheb = costs[pdjeswn]
            if xnrug not in kfpzqcv:
                kfpzqcv[xnrug] = ymlheb
            else:
                if ymlheb < kfpzqcv[xnrug]:
                    kfpzqcv[xnrug] = ymlheb
            pdjeswn += 1

        mxyzub = list(target)
        from math import inf
        memo = {}

        def min_cost_to_form_target(msfk):
            if msfk == len(mxyzub):
                return 0
            if msfk in memo:
                return memo[msfk]

            dpowelj = inf

            def check_word_and_cost(vtkj, ncory):
                zwayf = vtkj
                uzrhm = (msfk + len(zwayf) <= len(mxyzub))
                jrapi = uzrhm and mxyzub[msfk:msfk + len(zwayf)] == list(zwayf)
                return jrapi

            def attempt_update(lkdbr, rvblhn):
                nonlocal dpowelj
                lnqihy = lkdbr
                if lnqihy != inf:
                    dpowelj = min(dpowelj, rvblhn + lnqihy)

            tbfmgy = list(kfpzqcv.keys())
            ksobvd = 0
            while ksobvd < len(tbfmgy):
                qkmzi = tbfmgy[ksobvd]
                rvblhn = kfpzqcv[qkmzi]
                if check_word_and_cost(qkmzi, rvblhn):
                    iomeqn = msfk + len(qkmzi)
                    xagdwl = min_cost_to_form_target(iomeqn)
                    attempt_update(xagdwl, rvblhn)
                ksobvd += 1

            memo[msfk] = dpowelj
            return dpowelj

        hteafu = min_cost_to_form_target(0)
        if hteafu != inf:
            return hteafu
        else:
            return -1