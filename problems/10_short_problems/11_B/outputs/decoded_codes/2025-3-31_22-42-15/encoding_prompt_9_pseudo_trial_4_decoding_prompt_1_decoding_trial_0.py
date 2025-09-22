# 1. Begin
# 2. Declare a variable absoluteValue and set it to the absolute value of the integer input from the user
absoluteValue = abs(int(input()))

# 3. Initialize a variable currentIndex to 0
currentIndex = 0

# 4. Start an indefinite loop (repeat until a break condition is met)
while True:
    # 1. Calculate the sum of the first currentIndex natural numbers and store it in sumOfNumbers
    sumOfNumbers = (currentIndex * (currentIndex + 1)) / 2
    
    # 2. Calculate the difference as sumOfNumbers - absoluteValue
    difference = sumOfNumbers - absoluteValue
    
    # 3. If sumOfNumbers equals absoluteValue, then:
    if sumOfNumbers == absoluteValue:
        # 1. Print currentIndex
        print(currentIndex)
        # 2. Exit the loop
        break
    
    # 4. Else if sumOfNumbers is greater than absoluteValue, then:
    elif sumOfNumbers > absoluteValue:
        # 1. If difference is even, then:
        if difference % 2 == 0:
            # 1. Print currentIndex
            print(currentIndex)
            # 2. Exit the loop
            break
            
    # 5. Increment currentIndex by 1
    currentIndex += 1

# 5. End
