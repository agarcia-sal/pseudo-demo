# Step 1: Begin the program

# Step 2: Get an input value from the user and convert it to an absolute integer
inputNumber = abs(int(input()))

# Step 3: Initialize the counter variable "index" to 0
index = 0

# Step 4: Start an infinite loop
while True:
    # Step 4.1: Calculate the sum of integers from 0 to "index"
    sumOfIntegers = (index * (index + 1)) // 2
    
    # Step 4.2: Calculate "difference"
    difference = sumOfIntegers - inputNumber
    
    # Step 4.3: Check if "sumOfIntegers" is equal to "inputNumber"
    if sumOfIntegers == inputNumber:
        print(index)  # Print the value of "index"
        break  # Exit the loop
    
    # Step 4.4: Otherwise, if "sumOfIntegers" is greater than "inputNumber"
    elif sumOfIntegers > inputNumber:
        # Check if the "difference" is an even number
        if difference % 2 == 0:
            print(index)  # Print the value of "index"
            break  # Exit the loop
    
    # Step 4.5: Increment "index" by 1
    index += 1

# Step 5: End the program
