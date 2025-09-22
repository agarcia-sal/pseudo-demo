def main():
    # Step 1: Accept user input
    input1 = input()
    input2 = input()

    # Step 2: Split the inputs into individual numbers
    numbers1 = input1.split()
    numbers2 = input2.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare the corresponding values in both lists
    for index in range(3):
        value1 = numbers1[index]
        value2 = numbers2[index]

        # Step 5: Check if the numbers differ
        if value1 != value2:
            differenceCount += 1

    # Step 6: Determine the output based on differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Call the main function to execute the program
main()
