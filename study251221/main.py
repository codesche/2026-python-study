
# 리스트 인덱싱 & 슬라이싱
nums = [10, 20, 30, 40, 50]

print(nums[0])      # 10
print(nums[-1])     # 50
print(nums[1:4])    # [20, 30, 40]

nums.append(60)
nums.sort()
nums.reverse()
print(len(nums))

# 문자열 메서드
msg = " hello python "
print(msg.strip())          # 양쪽 공백 제거
print(msg.replace("python", "world"))

# 실전 예제 1: 문자열에서 단어 개수 세기
sentence = "python is easy and powerful"
words = sentence.split()
print(len(words))

# 실전 예제 2: 특정 문자 개수 세기 - 반복문 없이 해결 가능
text = "banana"
count = text.count("a")
print(count)

# 실전 예제 3: 리스트에서 짝수만 추출, 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)