def main():
    # Step 1: Accept user input for two lines of numbers
    line1 = input()
    line2 = input()

    # Step 2: Split the input lines into lists of strings
    numbers1 = line1.split()
    numbers2 = line2.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each pair of numbers
    for index in range(3):  # Looping over three pairs
        # Step 4a: Convert the strings to integers for comparison
        number1 = int(numbers1[index])
        number2 = int(numbers2[index])

        # Step 4b: Check if the two numbers differ
        if number1 != number2:
            difference_count += 1  # Increment count if numbers are different
    
    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # The pairs differ in less than three positions
    else:
        print("NO")   # The pairs differ in three or more positions

# Execute the main function when the program starts
main()
