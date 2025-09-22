# Function to find the first index where the sum of the first index natural numbers 
# meets the specified conditions relative to the input value
def find_index():
    # Step 1: Input
    # Reading an integer value from the user and calculating its absolute value
    targetNumber = abs(int(input()))

    # Step 2: Initialize the index counter
    index = 0

    # Step 3: Start an infinite loop to find the desired index
    while True:
        # Calculate the current sum of the first 'index' natural numbers
        currentSum = index * (index + 1) // 2  # Using integer division

        # Calculate the difference between the current sum and the target number
        difference = currentSum - targetNumber
        
        # Step 3.3: Check conditions
        if currentSum == targetNumber:
            # Case where the current sum is exactly the target number
            print(index)
            break
        elif currentSum > targetNumber:
            # Case where the current sum is greater than the target number
            if difference % 2 == 0:
                # Check if the difference is even
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Invoke the function to run the code
find_index()
