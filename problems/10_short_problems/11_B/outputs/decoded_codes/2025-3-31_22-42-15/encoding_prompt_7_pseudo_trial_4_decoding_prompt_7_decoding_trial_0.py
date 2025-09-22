def findIntegerWithSpecificProperty():
    # Read input from user and convert it to an integer
    inputValue = int(input())
    
    # Initialize absoluteValue as the absolute of inputValue
    absoluteValue = abs(inputValue)
    
    # Initialize index to 0
    index = 0
    
    # Start an infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' integers
        sumOfFirstIndex = (index * (index + 1)) // 2
        
        # Calculate the difference between sumOfFirstIndex and absoluteValue
        difference = sumOfFirstIndex - absoluteValue
        
        # Check if the sum equals the absolute value
        if sumOfFirstIndex == absoluteValue:
            print(index)
            break
        
        # Check if the sum is greater than the absolute value
        elif sumOfFirstIndex > absoluteValue:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index by 1 for the next iteration
        index += 1
