# Begin the program

# Get an input value from the user and convert it to an absolute integer.
inputNumber = abs(int(input()))

# Initialize a counter variable "index" to 0.
index = 0

# Start an infinite loop
while True:
    # Calculate the sum "sumOfIntegers" as the total of all integers from 0 to "index".
    sumOfIntegers = (index * (index + 1)) // 2  # Using integer division for accuracy

    # Calculate "difference" by subtracting "inputNumber" from "sumOfIntegers".
    difference = sumOfIntegers - inputNumber

    # Check if "sumOfIntegers" is equal to "inputNumber"
    if sumOfIntegers == inputNumber:
        print(index)  # Print the value of "index"
        break  # Exit the loop
        
    # Otherwise, if "sumOfIntegers" is greater than "inputNumber"
    elif sumOfIntegers > inputNumber:
        # Check if the "difference" is an even number
        if difference % 2 == 0:  # If true
            print(index)  # Print the value of "index"
            break  # Exit the loop

    # Increment "index" by 1.
    index += 1

# End the program
