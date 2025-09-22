# 1. Start the program

# 2. Get the absolute value of user input as an integer, assign it to `n`
n = abs(int(input()))

# 3. Initialize `i` to 0
i = 0

# 4. Enter an infinite loop
while True:
    # 4.1 Calculate the sum `s` of the first `i` natural numbers
    s = i * (i + 1) // 2  # Using integer division

    # 4.2 Calculate the difference `m` between `s` and `n`
    m = s - n

    # 4.3 Check if `s` is equal to `n`
    if s == n:
        print(i)  # Print the value of `i`
        break  # Exit the loop

    # 4.4 Check if `s` is greater than `n`
    elif s > n:
        # If this condition holds true, then check if `m` is even
        if m % 2 == 0:
            print(i)  # Print the value of `i`
            break  # Exit the loop

    # 4.5 Increment `i` by 1
    i += 1  # Continuously increase i
# 5. End of program
