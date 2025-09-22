def main():
    # Step 2: Prompt the user for input
    userInput1 = input()
    userInput2 = input()

    # Step 3: Split the input strings into individual components
    valueList1 = userInput1.split()
    valueList2 = userInput2.split()

    # Step 4: Initialize a counter for differences
    differenceCounter = 0

    # Step 5: Compare the corresponding values from both lists
    for index in range(3):  # Only need to check indices 0 to 2
        valueA = int(valueList1[index])  # Convert to integer
        valueB = int(valueList2[index])  # Convert to integer
        if valueA != valueB:
            differenceCounter += 1  # Increment counter for differences

    # Step 6: Evaluate the total differences
    if differenceCounter < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Step 1: Start the program
if __name__ == "__main__":
    main()


1 2 3
1 2 4
