n = int(input())
markings = [True] * n
index = 0
step = 1

while step <= 500000:
    if markings[index]:
        markings[index] = False
    step += 1
    index = (index + step) % n

remainingTrue = [item for item in markings if item]

if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")


def marking_process(n):
    markings = [True] * n
    current_position = 0
    current_step = 1

    while current_step <= 500000:
        if markings[current_position]:
            markings[current_position] = False
        current_step += 1
        current_position = (current_position + current_step) % n

    if not any(markings):
        print("YES")
    else:
        print("NO")

n = int(input())
marking_process(n)
