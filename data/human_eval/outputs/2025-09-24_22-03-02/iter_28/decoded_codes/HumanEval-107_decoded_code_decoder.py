def even_odd_palindrome(n):
    def is_palindrome(n):
        str_n = []
        temp_n = n
        while temp_n > 0:
            digit = temp_n % 10
            str_n.append(digit)
            temp_n = temp_n // 10
        reversed_str_n = []
        for index in range(len(str_n) - 1, -1, -1):
            reversed_str_n.append(str_n[index])
        original_str = ""
        for index in range(len(str_n)):
            original_str += str(str_n[index])
        reversed_str = ""
        for index in range(len(reversed_str_n)):
            reversed_str += str(reversed_str_n[index])
        if original_str == reversed_str:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n + 1):
        if i % 2 == 1 and is_palindrome(i) == True:
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i) == True:
            even_palindrome_count += 1

    return [even_palindrome_count, odd_palindrome_count]