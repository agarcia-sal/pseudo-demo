def find_minimal_i(n):
    # Ensure n is a non-negative integer
    n = abs(n)
    
    # Initialize counter 'i' to zero
    i = 0
    
    # Continue exploring potential solutions indefinitely
    while True:
        # Calculate the sum of the first 'i' numbers
        sum_of_first_i = (i * (i + 1)) // 2
        
        # Calculate the difference between sum_of_first_i and n
        difference = sum_of_first_i - n
        
        # Check if the sum equals n
        if sum_of_first_i == n:
            print(i)
            break
        
        # Check if the sum exceeds the input number
        elif sum_of_first_i > n:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(i)
                break
        
        # Increment i to check the next number
        i += 1

# Read input from the user
n = int(input())
find_minimal_i(n)
