# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    n = len(arr)
    d = d % n # Ensure the rotations are within the range of the array length

    left_rotated_arr = arr[d:] + arr[:d]

    return left_rotated_arr

# Test 
print(rotateLeft(4, [1, 2, 3, 4, 5]))


