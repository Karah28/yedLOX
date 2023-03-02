def binary(arr, x):
    low = 0
    high = len(arr) - 1
    middle = 0

    while low <= high:

        middle = (high + low) // 2

        if arr[middle] < x:
            low = middle + 1

        elif arr[middle] > x:
            high = middle - 1

        else:
            return True

    return False


arr = [1, 4, 6, 8, 10]
x = 6

result = binary(arr, x)

if result:
    print("True")
else:
    print("False")