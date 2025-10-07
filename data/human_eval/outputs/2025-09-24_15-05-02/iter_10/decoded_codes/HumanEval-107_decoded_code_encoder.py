def even_odd_palindrome(n):
    def is_palindrome(x):
        str_x = str(x)
        reversed_str_x = str_x[::-1]
        return str_x == reversed_str_x

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        if i % 2 == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i):
            even_palindrome_count += 1

    return even_palindrome_count, odd_palindrome_count