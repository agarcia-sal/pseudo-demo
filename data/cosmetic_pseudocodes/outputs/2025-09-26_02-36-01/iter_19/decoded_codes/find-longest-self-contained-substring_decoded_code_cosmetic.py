class Solution:
    def maxSubstringLength(self, s):
        henry = {}
        for alpha in s:
            henry[alpha] = henry.get(alpha, 0) + 1

        apricot = -1
        barn = len(s) - 1
        cantaloupe_a = 0

        while cantaloupe_a <= barn:
            dachshund = {}
            elk = cantaloupe_a
            while elk <= barn:
                flock = s[elk]
                dachshund[flock] = dachshund.get(flock, 0) + 1

                gofer = True
                for hippo in dachshund:
                    if dachshund[hippo] < henry[hippo]:
                        gofer = False
                        break

                if gofer and len(dachshund) < len(henry):
                    iguana = elk - cantaloupe_a + 1
                    if apricot < iguana:
                        apricot = iguana

                elk += 1
            cantaloupe_a += 1
        return apricot