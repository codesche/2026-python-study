
# 리스트 기본 연산
nums = [1, 2, 3, 4, 5]

print(nums[0])      # 1
print(nums[-1])     # 5
print(nums[1:4])    # [2, 3, 4]

nums.append(6)
nums.remove(3)      # 값 기준
print(nums)         # [1, 2, 4, 5, 6]

# 정렬
nums = [5, 1, 4, 2, 3]
nums.sort()
print(nums)     # [1, 2, 3, 4, 5]

nums.sort(reverse=True)     # 역순 정렬 허용: True
print(nums)

# 정렬된 리스트에서 합이 target이 되는 두 수 찾기
# 투 포인터, 브루트포스 O(n^2) -> 투 포인터 O(n)
nums = [1, 2, 3, 4, 6, 8, 9]
target = 10

left = 0
right = len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]

    if current_sum == target:
        print(nums[left], nums[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

# 연속 부분합 - 연속된 숫자의 합이 target 이상이 되는 최소 길이
nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
min_length = float('inf')

for right in range(len(nums)):
    current_sum += nums[right]

    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1

print(min_length)   # 2

# 중복 제거 (정렬된 리스트)
nums = [1, 1, 2, 2, 3, 3, 3, 4]

unique = []
prev = None

for n in nums:
    if n != prev:
        unique.append(n)
        prev = n

print(unique)       # [1, 2, 3, 4]












