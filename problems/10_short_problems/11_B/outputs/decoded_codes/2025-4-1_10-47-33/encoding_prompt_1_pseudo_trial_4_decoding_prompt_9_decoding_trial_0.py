# Start the program
inputNumber = abs(int(input()))  # Get user input, convert to absolute integer
index = 0  # Initialize the index counter

# Begin an infinite loop
while True:
    # Calculate the sum of integers from 0 to index using the formula
    sumOfIntegers = (index * (index + 1)) // 2
    # Calculate the difference
    difference = sumOfIntegers - inputNumber
    
    # Check if sumOfIntegers equals inputNumber
    if sumOfIntegers == inputNumber:
        print(index)  # Print the value of index
        break  # Exit the loop
    
    # Check if sumOfIntegers is greater than inputNumber
    elif sumOfIntegers > inputNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Print the value of index
            break  # Exit the loop
    
    # Increment index by 1
    index += 1
