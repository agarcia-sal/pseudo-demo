def main():
    # Read two lines of input from the user
    line1 = input()
    line2 = input()

    # Split the input lines into lists of strings
    numbers1 = line1.split()
    numbers2 = line2.split()

    # Initialize a variable to count the differences
    differenceCount = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current element from both lists to integers
        number1 = int(numbers1[index])
        number2 = int(numbers2[index])
        
        # Check if the two numbers are different
        if number1 != number2:
            # Increment the difference count
            differenceCount += 1

    # Check the number of differences found
    if differenceCount < 3:
        # Print "YES" if the number of differences is less than 3
        print("YES")
    else:
        # Print "NO" if the number of differences is 3 or more
        print("NO")

# Start the program execution
main()
