userInput = input()  # Get user input as a string
number = abs(int(userInput))  # Convert to integer and take absolute value


index = 0  # Initialize index variable


while True:  # Start infinite loop


    sum = (index * (index + 1)) / 2  # Calculate sum
    

    difference = sum - number  # Calculate difference
    

    if sum == number:  # Check if sum equals number
        print(index)  # Output current index
        break  # Exit the loop
    

    elif sum > number:  # Check if sum exceeds number
    

        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output current index
            break  # Exit the loop
    

    index += 1  # Increment index
    

userInput = input()  # Get user input as a string
number = abs(int(userInput))  # Convert to integer and take absolute value

index = 0  # Initialize index variable

while True:  # Start infinite loop
    sum = (index * (index + 1)) / 2  # Calculate sum
    difference = sum - number  # Calculate difference

    if sum == number:  # Check if sum equals number
        print(index)  # Output current index
        break  # Exit the loop
    elif sum > number:  # Check if sum exceeds number
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output current index
            break  # Exit the loop
            
    index += 1  # Increment index
