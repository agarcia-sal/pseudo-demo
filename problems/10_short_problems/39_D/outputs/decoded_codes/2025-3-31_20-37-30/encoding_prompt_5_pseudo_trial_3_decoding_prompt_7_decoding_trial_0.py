def main():
    # Step 1: Accept user input for two sets of three numbers each
    input1 = input()
    input2 = input()

    # Step 2: Split the inputs into individual numbers and convert them to integers
    numbers1 = list(map(int, input1.split()))
    numbers2 = list(map(int, input2.split()))

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare the corresponding values in both lists
    for index in range(3):  # Since we are only comparing three numbers
        value1 = numbers1[index]
        value2 = numbers2[index]

        # Step 5: Check if the numbers differ
        if value1 != value2:
            # If they differ, increment the difference counter
            differenceCount += 1

    # Step 6: Determine the output based on differences
    if differenceCount < 3:  
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" otherwise

# Step 7: Call the main function to execute the program
main()
