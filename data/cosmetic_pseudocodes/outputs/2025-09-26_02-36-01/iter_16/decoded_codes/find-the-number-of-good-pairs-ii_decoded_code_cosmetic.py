class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        val_mxgc = {}
        bmitjr = 0

        # Count occurrences of elements in nums2
        for cwrqby in nums2:
            val_mxgc[cwrqby] = val_mxgc.get(cwrqby, 0) + 1

        # For each element in nums1, check divisibility condition on keys of val_mxgc
        for aslpbr in nums1:
            for vemcot in val_mxgc.keys():
                if aslpbr % (vemcot * k) == 0:
                    bmitjr += val_mxgc[vemcot]

        return bmitjr