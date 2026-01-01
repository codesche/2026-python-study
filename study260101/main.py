
# 문자열은 불변, 수정하려면 새 문자열 생성

s = "hello"

print(len(s))   # 5
print(s[0])     # h
print(s[-1])    # o
print(s[1:4])   # ell (start, end - 1)

s = "hello"
s = s.replace("h", "H")
print(s)        # Hello

# 문자열 반복 & 조건 처리
# 문자열 = 문자(char)의 리스트처럼 다룬다
word = "banana"

for ch in word:
    print(ch)

# 빈도수 문제 기본 패턴 (dict)
## 예제: 문자 빈도수 세기
text = "banana"
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)     # {'b': 1, 'a': 3, 'n': 2}

# get()을 사용한 빈도수
text = "apple"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# 가장 많이 나온 문자 찾기
text = "aabbbcddddd"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

max_char = ""
max_count = 0

for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

print(max_char, max_count)

# 단어 빈도수 (공백 기준)
sentence = "hello world hello python"
words = sentence.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)

# 문자열 뒤집기
s = "python"
reversed_s = ""

for ch in s:
    reversed_s = ch + reversed_s        # 뒤쪽에서 reversed_s + ch 를 하면 정방향으로 출력

print(reversed_s)
print(s[::-1])