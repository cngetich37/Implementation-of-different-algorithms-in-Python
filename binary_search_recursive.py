arr_one = [1, 6, 9, 13, 24, 36, 40]


def binary_search_two(arr, leftmost, rightmost, target):

    if rightmost >= leftmost:
        mid = (rightmost + leftmost) // 2
        if target == arr[mid]:
            return "number " + str(arr[mid]) + " found"
        else:
            if target > arr[mid]:
                return binary_search_two(arr, leftmost, mid+1, target)
            else:
                return binary_search_two(arr, rightmost, mid - 1, target)
    else:
        return " not found, please try again"


print(binary_search_two(arr_one, 0, len(arr_one)-1, 13))
