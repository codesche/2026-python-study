
# 기본 이진 탐색 구현 - 찾고 싶은 값이 있는지 여부
# left <= right, O(log n)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))   # True
print(binary_search(nums, 4))   # False