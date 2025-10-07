class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            local_Alpha = 0
            local_Bravo = set()
            iterator_local_Charlie = 0
            while iterator_local_Charlie < len(s):
                local_Delta = s[iterator_local_Charlie]
                if len(local_Bravo) < k:
                    local_Bravo.add(local_Delta)
                else:
                    if local_Delta not in local_Bravo:
                        local_Alpha += 1
                        local_Bravo = {local_Delta}
                iterator_local_Charlie += 1

            if len(local_Bravo) > 0:
                local_Alpha += 1
            return local_Alpha

        external_Foxtrot = max_partitions(s, k)
        local_Echo = 0
        while local_Echo < len(s):
            local_Golf = 'z'
            local_Hotel = 'a'
            while local_Hotel <= local_Golf:
                if local_Hotel != s[local_Echo]:
                    local_India = s[:local_Echo]
                    local_Juliett = s[local_Echo + 1:]
                    local_Mike = local_India + local_Hotel + local_Juliett
                    candidate = max_partitions(local_Mike, k)
                    if candidate > external_Foxtrot:
                        external_Foxtrot = candidate
                local_Hotel = chr(ord(local_Hotel) + 1)
            local_Echo += 1
        return external_Foxtrot