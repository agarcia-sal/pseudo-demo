def find_integer():
    # Convert the input to an absolute integer
    n = abs(int(input()))
    
    # Initialize counter variable
    i = 0
    
    # Start an infinite loop
    while True:
        # Calculate the sum of the first i integers using the formula (i * (i + 1)) / 2
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and the target number
        m = s - n
        
        # Check if the current sum equals the target number
        if s == n:
            print(i)
            break
        
        # Check if the current sum exceeds the target number
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
        
        # Increment the counter for the next iteration
        i += 1

# Test cases to ensure function works as expected
if __name__ == "__main__":
    # Test cases examples to validate the functionality
    print("Test case 1: input 3")
    find_integer()  # Expected output: 2 since 0 + 1 + 2 = 3
    
    print("Test case 2: input 5")
    find_integer()  # Expected output: 5 since 0 + 1 + 2 + 3 + 4 + 5 = 15 and 15 - 5 = 10 (even)

    print("Test case 3: input 0")
    find_integer()  # Expected output: 0 since 0 == 0

    print("Test case 4: input 10")
    find_integer()  # Expected output: 4, because if the total reaches 10, we can get SUM(0,1,2,3,4) = 10
    
    print("Test case 5: input 15")
    find_integer()  # Expected output: 5
    
    print("Test case 6: input 20")
    find_integer()  # Expected output: 6
