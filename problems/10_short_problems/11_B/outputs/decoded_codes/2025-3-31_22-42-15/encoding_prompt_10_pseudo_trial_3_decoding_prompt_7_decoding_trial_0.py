# Function to find the integer i such that:
# 1. The sum of the first i natural numbers equals the input n, or 
# 2. The difference between the sum and n is even when the sum exceeds n.
def find_integer():
    # Step 2: Declare integer variable n and read its absolute value
    n = abs(int(input()))
    # Step 4: Declare integer variable i and initialize it to 0
    i = 0

    # Step 5: Start the infinite while loop
    while True:
        # Step 6: Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Use integer division to prevent floating-point results
        # Step 7: Calculate the difference between s and n
        m = s - n

        # Step 8: Check if the sum equals n
        if s == n:
            print(i)  # Step 9: Output the value of i
            break  # Step 10: Exit the loop

        # Step 11: Check if the sum is greater than n
        elif s > n:
            # Step 12: Check if the difference m is even
            if m % 2 == 0:  # Modulus operator to check for even number
                print(i)  # Step 13: Output the value of i
                break  # Step 14: Exit the loop

        # Step 15: Increment i by 1 to check the next integer
        i += 1  # Move to the next integer

# Call the function to execute the logic
find_integer()
