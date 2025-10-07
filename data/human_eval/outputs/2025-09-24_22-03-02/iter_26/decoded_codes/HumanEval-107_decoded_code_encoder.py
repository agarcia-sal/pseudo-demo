def even_odd_palindrome(n):
    def is_palindrome(n):
        string_n = str(n)
        reversed_string = string_n[::-1]
        return string_n == reversed_string

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        remainder = i % 2
        palindrome_check = is_palindrome(i)
        if remainder == 1 and palindrome_check:
            odd_palindrome_count += 1
        elif remainder == 0 and palindrome_check:
            even_palindrome_count += 1

    return (even_palindrome_count, odd_palindrome_count)