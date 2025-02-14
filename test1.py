def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        # BUG: The intended calculation is (low + high) // 2,
        # but due to operator precedence, this computes as low + (high // 2)
        mid = low + high // 2  
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test the binary_search function
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11]
    target = 7
    index = binary_search(sorted_list, target)
    print("Index of {} is: {}".format(target, index))
