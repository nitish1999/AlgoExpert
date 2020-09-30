# O(Log(n)) time | O(Log(n)) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1

    middle = (left+right)//2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle-1)
    else:
        return binarySearchHelper(array, target, middle+1, right)

# O(Log(n)) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        middle = (left+right)//2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle-1
        else:
            left = middle+1
    return -1

print(binarySearch([2,3,5,7,9], 5))
