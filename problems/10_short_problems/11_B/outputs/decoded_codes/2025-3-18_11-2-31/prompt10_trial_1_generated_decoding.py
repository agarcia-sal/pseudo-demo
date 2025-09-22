def main():
    # Step 2: Declare integer variable n and assign the absolute value of the user input
    n = abs(int(input()))
    
    # Step 4: Declare integer variable i and initialize to 0
    i = 0

    # Step 5: Start an infinite loop
    while True:
        # Step 6: Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2  # Use integer division to avoid float results
        m = s - n  # Step 7: Calculate m
        
        # Step 8: Check if s is equal to n
        if s == n:
            print(i)  # Step 9: Print i
            break  # Step 10: Break the loop
        
        # Step 11: Check if s is greater than n
        elif s > n:
            # Step 12: Check if m is even
            if m % 2 == 0:  # Check evenness
                print(i)  # Step 13: Print i
                break  # Step 14: Break the loop
        
        # Step 15: Increment i by 1
        i += 1

# Step 1: Call the main function
if __name__ == "__main__":
    main()
