
# 기본 정렬
nums = [4, 1, 7, 3, 2]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# 기준(key) 정렬
words = ["apple", "banana", "kiwi"]
words.sort(key=len)     # 길이 기준으로 정렬
print(words)            # ['kiwi', 'apple', 'banana']

# 튜플 / 리스트 정렬
data = [(1, 3), (4, 1), (2, 2)]
data.sort(key=lambda x: x[1])           # 뒷 요소 기준으로 정렬
print(data)     # [(4, 1), (2, 2), (1, 3)]

# 동전 거스름돈 (Greedy)
coins = [500, 100, 50, 10]
money = 1260

count = 0
for coin in coins:
    count += money // coin
    money %= coin

print(count)    # 6

# 회의실 배정 - 최대 회의 개수 선택
meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]

## 끝나는 시간 기준 정렬
meetings.sort(key=lambda x: x[1])

end_time = 0
count = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)

# 최소 대기시간 (Greedy + 정렬)
## 짧은 작업부터 처리 = 전체 대기시간 최소
times = [3, 1, 4, 3, 2]
times.sort()        # [1, 2, 3, 3, 4]

total = 0
current = 0

for t in times:
    current += t
    total += current

print(total)
