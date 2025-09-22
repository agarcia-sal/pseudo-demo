def main():
    inputString = input()
    normalizedPath = NormalizePath(inputString)
    finalPath = RemoveLeadingSlashes(normalizedPath)
    print(finalPath)

def NormalizePath(path):
    # Normalize the path by converting backslashes to forward slashes
    # and removing unnecessary segments from the path
    path = path.replace('\\', '/')
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

    return '/'.join(stack)

def RemoveLeadingSlashes(path):
    if path.startswith('/'):
        return '/' + path.lstrip('/')
    else:
        return path

if __name__ == "__main__":
    main()
