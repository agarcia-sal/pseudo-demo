class Solution:
    def countDays(self, days, meetings):
        def customSort(arr):
            if len(arr) < 2:
                return
            pivot_index = 0
            pivot_value = arr[pivot_index][1]
            less_list = []
            greater_list = []
            for i in range(1, len(arr)):
                if arr[i][1] < pivot_value:
                    less_list.append(arr[i])
                else:
                    greater_list.append(arr[i])
            customSort(less_list)
            customSort(greater_list)
            idx = 0
            for item in less_list:
                arr[idx] = item
                idx += 1
            arr[idx] = arr[pivot_index]
            idx += 1
            for item in greater_list:
                arr[idx] = item
                idx += 1

        customSort(meetings)

        xrlp = 1
        qronaf = 0

        def loopProcess(jbsx):
            nonlocal xrlp, qronaf
            if len(jbsx) == 0:
                return
            isunf = jbsx[0]
            pgajy = isunf[1]
            ftovz = isunf[2]

            if xrlp < pgajy:
                qronaf += (pgajy - xrlp)
            if ftovz + 1 > xrlp:
                xrlp = ftovz + 1

            loopProcess(jbsx[1:])

        loopProcess(meetings)

        if xrlp <= days:
            qronaf += (days - xrlp + 1)

        return qronaf