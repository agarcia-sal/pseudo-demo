def main():
    # Prompt the user for input
    userInput1 = input()
    userInput2 = input()
    
    # Split the input strings into lists
    valueList1 = userInput1.split()
    valueList2 = userInput2.split()
    
    # Initialize a counter for differences
    differenceCounter = 0
    
    # Compare the corresponding values from both lists
    for index in range(3):  # Loop through indices 0 to 2
        valueA = int(valueList1[index])  # Convert indexed value from list 1 to integer
        valueB = int(valueList2[index])  # Convert indexed value from list 2 to integer
        
        # Check for differences
        if valueA != valueB:
            differenceCounter += 1  # Increment counter if values are different
    
    # Evaluate the total differences
    if differenceCounter < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Start the program
if __name__ == "__main__":
    main()
