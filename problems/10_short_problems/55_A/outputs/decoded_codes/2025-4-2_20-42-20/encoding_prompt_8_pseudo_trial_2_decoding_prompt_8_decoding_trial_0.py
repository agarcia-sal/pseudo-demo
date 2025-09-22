# Initialize Variables
n = int(input())
b = [True] * n
j = 0
i = 1

# Iterate to Mark Values
while i <= 500000:
    if b[j]:  # Check if the current index `j` in list `b` is 'True'
        b[j] = False  # Mark the value at index `j` as 'False'
    i += 1
    j = (j + i) % n  # Update `j` using the modulo operation

# Check Remaining True Values
if all(not value for value in b):  # Create a new list `x` that contains only the 'True' values
    print("YES")  # Output "YES" if no 'True' values remain
else:
    print("NO")  # Otherwise, output "NO"


def mark_values(n):
    b = [True] * n
    j, i = 0, 1

    while i <= 500000:
        if b[j]:
            b[j] = False
        i += 1
        j = (j + i) % n

    return all(not value for value in b)

def main():
    n = int(input())
    if mark_values(n):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
