def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n = -n
            neg = -1
        n = [int(d) for d in str(n)]
        n[0] *= neg
        return sum(n)

    list_of_sums = [digits_sum(i) for i in arr]
    filtered_list = [x for x in list_of_sums if x > 0]
    return len(filtered_list)