# Given a string path, which is an absolute path (starting with a slash '/') to a file 
# or directory in a Unix-style file system, convert it to the simplified canonical path

def simplify_path(path):

    # Split the path into components 
    parts = path.split('/')
    stack = []

    for part in parts: 
        if part == '..':
            # Pop the last valid directory from the stack if '..' which signifies going back one directory
            if stack: 
                stack.pop()
        elif part and part != '.':
            # If the part is not empty or '.' (which signifies current directory), add it to the stack
            stack.append(part)

    # Join the parts together with '/' to form the simplified path
    # If the stack is empty, we have the root path, "/"
    return '/' + '/'.join(stack)

test_paths = {
    "/home/": "/home",
    "/../": "/",
    "/home//foo//": "/home/foo",
    "/etc/foo/../bar/file.txt": "/etc/bar/file.txt"
}

for test_path, expected in test_paths.items():
    assert simplify_path(test_path) == expected, f"Test failed for: {test_path}"

print("Tests passed successfully.")