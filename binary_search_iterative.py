arr_one = [1, 6, 9, 13, 24, 36, 40]
target_one = 6


def binary_search_one(arr, target):
    leftmost = 0
    rightmost = len(arr) - 1

    while leftmost <= rightmost:
        mid = (leftmost + rightmost) // 2
        if target == arr[mid]:
            return "The number is " + str(arr[mid])
        elif target > arr[mid]:
            leftmost = mid + 1
        else:
            rightmost = mid - 1
    return "not found, please try again"


print(binary_search_one(arr_one, target_one))
