
# bisect 모듈 (파이썬 내장)
from bisect import bisect_left, bisect_right

nums = [1, 3, 3, 3, 5, 7]

print(bisect_left(nums, 3))     # 1
print(bisect_right(nums, 3))    # 4

count = bisect_right(nums, 3) - bisect_left(nums, 3)
print(count)    # 3