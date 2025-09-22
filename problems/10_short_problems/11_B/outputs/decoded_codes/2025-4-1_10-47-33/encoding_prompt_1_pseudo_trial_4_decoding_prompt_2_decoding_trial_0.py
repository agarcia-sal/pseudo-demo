# Begin the program
# Step 2: Get an input value from the user and convert it to an absolute integer
inputNumber = abs(int(input()))

# Step 3: Initialize a counter variable "index" to 0
index = 0

# Step 4: Start an infinite loop
while True:
    # Step 1.1: Calculate the sum "sumOfIntegers"
    sumOfIntegers = (index * (index + 1)) // 2  # Using integer division

    # Step 1.2: Calculate "difference"
    difference = sumOfIntegers - inputNumber
    
    # Step 1.3: Check if "sumOfIntegers" is equal to "inputNumber"
    if sumOfIntegers == inputNumber:
        print(index)
        break  # Exit the loop
    
    # Step 1.4: Otherwise, check if "sumOfIntegers" is greater than "inputNumber"
    elif sumOfIntegers > inputNumber:
        # Step 1.4.1: Check if the "difference" is an even number
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop
    
    # Step 1.5: Increment "index" by 1
    index += 1

# End the program
