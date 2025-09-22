def main():
    # Read input values
    t1 = input()  # Get user input for the first string
    t2 = input()  # Get user input for the second string

    # Split the input strings into lists
    tt1 = t1.split()  # Split t1 into a list
    tt2 = t2.split()  # Split t2 into a list
    
    # Initialize the result counter
    differenceCount = 0 

    # Compare the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        a = int(tt1[index])  # Convert tt1[index] to integer
        b = int(tt2[index])  # Convert tt2[index] to integer
        if a != b:  # Check if a is not equal to b
            differenceCount += 1  # Increment differenceCount by 1

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")  # Print "NO" otherwise

# Execute the main function when the script runs
main()
