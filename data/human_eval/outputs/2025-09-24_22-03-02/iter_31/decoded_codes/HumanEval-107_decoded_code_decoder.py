def even_odd_palindrome(n):
    def is_palindrome(n):
        str_n = str(n)
        reversed_str = ''
        index = len(str_n) - 1
        while index >= 0:
            reversed_str += str_n[index]
            index -= 1
        return str_n == reversed_str

    even_palindrome_count = 0
    odd_palindrome_count = 0

    i = 1
    while i <= n:
        remainder = i % 2
        palindrome_check = is_palindrome(i)
        if remainder == 1 and palindrome_check:
            odd_palindrome_count += 1
        elif remainder == 0 and palindrome_check:
            even_palindrome_count += 1
        i += 1

    return even_palindrome_count, odd_palindrome_count