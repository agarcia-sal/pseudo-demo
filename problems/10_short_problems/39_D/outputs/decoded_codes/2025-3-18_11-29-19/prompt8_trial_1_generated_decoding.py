def main():
    # Step 1: Get input from the user
    firstSet = input()
    secondSet = input()

    # Step 2: Split the input strings into individual numbers
    numberList1 = firstSet.split()
    numberList2 = secondSet.split()

    # Step 3: Initialize a counter for differences
    differencesCount = 0

    # Step 4: Compare the corresponding numbers in both lists
    for index in range(3):
        # Convert the values to integers for comparison
        value1 = int(numberList1[index])
        value2 = int(numberList2[index])
        
        # Step 5: Check if the numbers are different
        if value1 != value2:
            differencesCount += 1

    # Step 6: Determine the result based on the count of differences
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
main()
