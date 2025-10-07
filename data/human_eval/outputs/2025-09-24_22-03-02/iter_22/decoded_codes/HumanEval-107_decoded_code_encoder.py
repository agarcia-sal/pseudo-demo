def even_odd_palindrome(n):
    def is_palindrome(n):
        str_n = str(n)
        reversed_str_n = ''
        length = len(str_n)
        index = length - 1
        while index >= 0:
            reversed_str_n += str_n[index]
            index -= 1
        return str_n == reversed_str_n

    even_palindrome_count = 0
    odd_palindrome_count = 0
    i = 1
    while i <= n:
        i_mod_2 = i % 2
        if i_mod_2 == 1:
            palindrome_check = is_palindrome(i)
            if palindrome_check:
                odd_palindrome_count += 1
        elif i_mod_2 == 0:
            palindrome_check = is_palindrome(i)
            if palindrome_check:
                even_palindrome_count += 1
        i += 1

    return (even_palindrome_count, odd_palindrome_count)