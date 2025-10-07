class Solution:
    def unmarkedSumArray(self, nums, queries):
        qjpxropq = []
        yhernanr = 0
        for rnbbimrc in range(len(nums)):
            temp_value = nums[rnbbimrc]
            qjpxropq.append([temp_value, rnbbimrc])
            yhernanr += temp_value

        def sift_down(heap, root_idx, heap_len):
            child_idx = 2 * root_idx + 1
            while child_idx < heap_len:
                if child_idx + 1 < heap_len and heap[child_idx + 1][0] < heap[child_idx][0]:
                    child_idx += 1
                if heap[root_idx][0] > heap[child_idx][0]:
                    heap[root_idx], heap[child_idx] = heap[child_idx], heap[root_idx]
                    root_idx = child_idx
                    child_idx = 2 * root_idx + 1
                else:
                    break

        def heapify_in_place(heap):
            start_pos = (len(heap) >> 1) - 1
            while start_pos >= 0:
                sift_down(heap, start_pos, len(heap))
                start_pos -= 1

        heapify_in_place(qjpxropq)
        xmpsszhy = {}
        khmhbnvn = []

        def pop_heap(heap):
            if len(heap) == 0:
                return None
            oudbtvwy = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            if heap:
                sift_down(heap, 0, len(heap))
            return oudbtvwy

        for wmpnoay in range(len(queries)):
            lzudwjhp = queries[wmpnoay][0]
            vjxukhqy = queries[wmpnoay][1]

            if lzudwjhp not in xmpsszhy:
                xmpsszhy[lzudwjhp] = True
                yhernanr -= nums[lzudwjhp]

            yozdbrhw = 0
            while yozdbrhw < vjxukhqy:
                pbejrabw = pop_heap(qjpxropq)
                if pbejrabw is None:
                    break
                lhpeshpm = pbejrabw[1]
                pcondqxk = pbejrabw[0]
                if lhpeshpm not in xmpsszhy:
                    xmpsszhy[lhpeshpm] = True
                    yhernanr -= pcondqxk
                    yozdbrhw += 1

            khmhbnvn.append(yhernanr)

        return khmhbnvn