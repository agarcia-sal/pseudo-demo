# Function to compare two sets of numerical inputs
def compare_number_sets():
    # Step 2: Receive Input
    firstSet = input()  # First set of numbers from user
    secondSet = input()  # Second set of numbers from user

    # Step 3: Split Input Strings into Lists
    numbersSet1 = firstSet.split()  # Split the first set into a list
    numbersSet2 = secondSet.split()  # Split the second set into a list

    # Step 4: Initialize a Counter
    differenceCount = 0  # Counter for differing positions

    # Step 5: Compare Each Position
    for index in range(3):  # We compare the first three positions (0, 1, 2)
        num1 = int(numbersSet1[index])  # Convert current value from the first set to an integer
        num2 = int(numbersSet2[index])  # Convert current value from the second set to an integer
        if num1 != num2:  # If numbers differ
            differenceCount += 1  # Increase the counter

    # Step 6: Output the Result
    if differenceCount < 3:  # Check if the differences are fewer than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Start the program
compare_number_sets()


  1 2 3
  1 2 3
  

  1 2 3
  1 3 3
  

  4 5 6
  7 8 9
  

  2 3 4
  2 3 5
  