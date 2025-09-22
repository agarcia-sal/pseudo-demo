def find_integer(n):
    # Step 1: Get absolute value of n
    n = abs(n)
    i = 0  # Step 2: Initialize i

    while True:  # Step 3: Start an infinite loop
        s = (i * (i + 1)) // 2  # Step 4: Calculate s
        m = s - n  # Step 5: Calculate m

        if s == n:  # Step 6: Check if s equals n
            print(i)  # Step 7: Print i
            break  # Step 8: Exit the loop

        elif s > n:  # Step 9: Check if s is greater than n
            if m % 2 == 0:  # Step 10: Check if m is even
                print(i)  # Step 11: Print i
                break  # Step 12: Exit the loop

        i += 1  # Step 13: Increment i

# Test the function with different inputs
test_cases = [0, 1, 2, 3, 4, 5, 10, -10, 15]
for num in test_cases:
    print(f"Input: {num}")
    find_integer(num)
