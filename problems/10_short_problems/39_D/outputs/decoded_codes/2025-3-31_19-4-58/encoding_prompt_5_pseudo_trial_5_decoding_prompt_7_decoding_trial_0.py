def main():
    # Read two lines of input from the user, each containing three numbers
    firstSet = input()  # Read the first set of numbers
    secondSet = input()  # Read the second set of numbers

    # Split the input strings into individual numbers
    firstNumbers = firstSet.split()  # Split the first set into a list of strings
    secondNumbers = secondSet.split()  # Split the second set into a list of strings

    # Initialize a count to track the number of differences
    differenceCount = 0 

    # Loop through the numbers in the two sets
    for index in range(3):  # Since there are 3 numbers, we loop from 0 to 2
        # Convert the current numbers from strings to integers
        firstNumber = int(firstNumbers[index])  # Convert to integer
        secondNumber = int(secondNumbers[index])  # Convert to integer
        
        # Check if the current numbers from both sets are different
        if firstNumber != secondNumber:  # If they are different
            differenceCount += 1  # Increment the difference count

    # After comparing all numbers, check the difference count
    if differenceCount < 3:  # If there are fewer than three differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     4 5 3
     

     1 2 3
     4 5 6
     