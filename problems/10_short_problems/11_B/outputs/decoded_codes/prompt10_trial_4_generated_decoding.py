def find_natural_number():
    # Step 1: Get user input and initialize n to its absolute value
    n = abs(int(input()))
    i = 0  # Step 2: Initialize variable i to 0

    while True:  # Step 3: Start an infinite loop
        # Step 3a: Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division for precision
        m = s - n  # Step 3b: Calculate m

        if s == n:  # Step 3c: Check if s equals n
            print(i)  # Step 3c.i: Print the value of i
            break  # Step 3c.ii: Exit the loop

        elif s > n:  # Step 3d: Check if s is greater than n
            if m % 2 == 0:  # Step 3d.i: Check if m is divisible by 2
                print(i)  # Print the value of i
                break  # Exit the loop

        i += 1  # Step 3e: Increment the value of i by 1

# Call the function to execute the logic
find_natural_number()
