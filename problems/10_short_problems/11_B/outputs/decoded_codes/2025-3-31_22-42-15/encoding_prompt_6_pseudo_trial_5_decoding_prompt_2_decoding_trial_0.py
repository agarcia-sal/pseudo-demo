# Read an integer input and convert it to its absolute value
inputNumber = abs(int(input()))

# Initialize a variable to keep track of the current index
currentIndex = 0

# Infinite loop to evaluate conditions
while True:
    # Calculate the sum of the first 'currentIndex' natural numbers
    sum = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference between the 'sum' and the input number
    difference = sum - inputNumber
    
    # Check if the calculated sum equals the input number
    if sum == inputNumber:
        # If true, print the current index and exit the loop
        print(currentIndex)
        break
    
    # Check if the calculated sum exceeds the input number
    elif sum > inputNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # If true, print the current index and exit the loop
            print(currentIndex)
            break
    
    # Increment the current index for the next iteration
    currentIndex += 1
