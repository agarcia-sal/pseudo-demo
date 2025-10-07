def even_odd_palindrome(n):
    def is_palindrome(n):
        str_n = str(n)
        reversed_str_n = ''
        for index in range(len(str_n) - 1, -1, -1):
            reversed_str_n += str_n[index]
        if str_n == reversed_str_n:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        is_i_palindrome = is_palindrome(i)
        if (i % 2) == 1 and is_i_palindrome:
            odd_palindrome_count += 1
        elif (i % 2) == 0 and is_i_palindrome:
            even_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)