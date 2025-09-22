# Function to find the integer i such that the sum of the first i natural numbers
# either equals the absolute value of the input number or satisfies certain conditions.

def find_natural_number():
    # Get user input and take its absolute value
    n = abs(int(input()))
    i = 0  # Initialize loop counter

    while True:  # Start infinite loop
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        m = s - n
        
        # Check if the sum is equal to the absolute input number
        if s == n:
            print(i)  # Print the value of i
            break  # Exit the loop
        
        # Check if the sum exceeds the input number
        if s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Print the value of i
                break  # Exit the loop
        
        # Increment loop counter
        i += 1
        
# Example test case call (included in comments as instructed)
# find_natural_number()  # Expected to wait for input and print the result based on that input
