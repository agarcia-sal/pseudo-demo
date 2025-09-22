def normalize_path(path):
    # Remove unnecessary components from the path
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    normalized_path = '/'.join(stack)
    
    # Format with a single leading slash
    if normalized_path:
        normalized_path = '/' + normalized_path

    return normalized_path

# Start Program
rawInput = input()
cleanedInput = rawInput.strip()

# Normalize the path
normalizedPath = normalize_path(cleanedInput)

# Output the result
print(normalizedPath)
