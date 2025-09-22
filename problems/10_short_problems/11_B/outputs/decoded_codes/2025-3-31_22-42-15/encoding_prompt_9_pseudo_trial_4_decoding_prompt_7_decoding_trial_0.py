# Step 1: Begin the logic of the algorithm

# Step 2: Read the input and calculate the absolute value
absoluteValue = abs(int(input()))

# Step 3: Initialize the current index
currentIndex = 0

# Step 4: Start the indefinite loop
while True:
    # Step 4.1: Calculate the sum of the first currentIndex natural numbers
    sumOfNumbers = (currentIndex * (currentIndex + 1)) // 2  # Using integer division to avoid float
    
    # Step 4.2: Calculate the difference
    difference = sumOfNumbers - absoluteValue
    
    # Step 4.3: Check if we equal the absolute value
    if sumOfNumbers == absoluteValue:
        print(currentIndex)  # Print the current index
        break  # Exit the loop
    
    # Step 4.4: Check if the sum exceeds the absolute value
    elif sumOfNumbers > absoluteValue:
        # Step 4.4.1: Check if the difference is even
        if difference % 2 == 0:
            print(currentIndex)  # Print the current index
            break  # Exit the loop
    
    # Step 4.5: Increment the current index
    currentIndex += 1

# Step 5: End of the logic, no need for additional code as we have already printed the result
