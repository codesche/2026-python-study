
# get()을 활용한 간결한 패턴
counter = {}

items = ["a", "b", "a", "c", "b", "a"]

# for item in items:
#     if item not in counter:
#         counter[item] = 1
#     else:
#         counter[item] += 1

for item in items:
    counter[item] = counter.get(item, 0) + 1

print(counter)

# 실전 예제 1: 문자열에서 가장 많이 등장한 문자
# max(dict, key=dict.get) 패턴은 필수 암기
text = "mississippi"
counter = {}

for ch in text:
    counter[ch] = counter.get(ch, 0) + 1

max_char = max(counter, key=counter.get)
print(max_char, counter[max_char])

# 실전 예제 2: 숫자 리스트에서 중복 여부 확인
numbers = [1, 2, 3, 4, 2, 5]
seen = {}

has_duplicate = False

for n in numbers:
    if n in seen:
        has_duplicate = True
        break
    seen[n] = True

print(has_duplicate)

# 실전 예제 3: 투표 결과 계산
votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
result = {}

for name in votes:
    result[name] = result.get(name, 0) + 1

winner = max(result, key=result.get)
print("Winner:", winner)

# 실전 예제 4: 두 문자열이 아나그램인지 확인
def is_anagram(a, b):
    if len(a) != len(b):
        return False

    counter = {}
    for ch in a:
        counter[ch] = counter.get(ch, 0) + 1

    for ch in b:
        if ch not in counter or counter[ch] == 0:
            return False
    counter[ch] -= 1

    return True

print(is_anagram("listen", "silent"))