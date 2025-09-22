# Function to find the smallest non-negative integer representing a triangular number 
# or can be adjusted to match the target number by removing an even number
def find_triangular_integer():
    # Step 1: Receive Input
    targetNumber = abs(int(input()))  # Convert input to absolute integer

    # Step 2: Initialize Variables
    currentInteger = 0  # This will track the current non-negative integer

    # Step 3: Start an Infinite Loop
    while True:
        # Step 4: Calculate Triangular Number
        triangularNumber = (currentInteger * (currentInteger + 1)) // 2  # Use integer division for exact result

        # Step 5: Determine the Difference
        difference = triangularNumber - targetNumber
        
        # Step 6: Check Conditions
        if triangularNumber == targetNumber:
            print(currentInteger)  # Output currentInteger
            break  # Exit the loop (valid number found)

        elif triangularNumber > targetNumber:
            if difference % 2 == 0:  # Check if the difference is even
                print(currentInteger)  # Output currentInteger (valid adjustment found)
                break  # Exit the loop

        # Step 7: Increment the Integer
        currentInteger += 1  # Move to the next integer

# Run the function to find the triangular integer
find_triangular_integer()
