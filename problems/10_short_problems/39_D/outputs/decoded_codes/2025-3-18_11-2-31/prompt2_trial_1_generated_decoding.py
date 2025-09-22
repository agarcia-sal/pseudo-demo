# Input: Read two lines of input
t1 = input()
t2 = input()

# Process: Split both input lines into separate elements
tt1 = t1.split()
tt2 = t2.split()

# Initialize a variable to count the differences
differenceCount = 0

# For each score position (0 to 2)
for i in range(3):
    # Convert the scores to integers
    scoreA = int(tt1[i])
    scoreB = int(tt2[i])
    
    # Compare the scores and increment differenceCount if they differ
    if scoreA != scoreB:
        differenceCount += 1

# Check the differenceCount to determine the output
if differenceCount < 3:
    print("YES")
else:
    print("NO")
