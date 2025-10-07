def count_nums(array_of_integers):
    def digits_sum(integer_n):
        neg = 1
        if integer_n < 0:
            integer_n = -integer_n
            neg = -1
        list_of_digits = [int(ch) for ch in str(integer_n)]
        list_of_digits[0] *= neg
        sum_of_digits = sum(list_of_digits)
        return sum_of_digits

    list_of_sums = [digits_sum(element) for element in array_of_integers]
    count = sum(1 for sum_value in list_of_sums if sum_value > 0)
    return count