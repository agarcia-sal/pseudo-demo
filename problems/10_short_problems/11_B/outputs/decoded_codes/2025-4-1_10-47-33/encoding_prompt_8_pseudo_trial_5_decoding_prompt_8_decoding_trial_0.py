# Start the Program
inputValue = abs(int(input()))

# Initialize a Counter
currentIndex = 0

# Create an Infinite Loop for Calculation
while True:
    # Calculate the Triangular Number
    triangularSum = (currentIndex * (currentIndex + 1)) // 2
    
    # Determine the Difference
    difference = triangularSum - inputValue

    # Check for Exact Match
    if triangularSum == inputValue:
        print(currentIndex)  # Output the value of currentIndex
        break
    
    # Check for Condition When Triangular Sum Exceeds Input Value
    if triangularSum > inputValue:
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)  # Output the value of currentIndex
            break
    
    # Increment the Counter
    currentIndex += 1

# End the Program


def calculate_triangular_number(n):
    return (n * (n + 1)) // 2
