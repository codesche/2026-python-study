# 🐍 Python Warm-up

파이썬의 기본 문법과 자료구조를 차근차근 학습하며  
**코딩 테스트 대응력 + 실무 감각**을 함께 기르는 개인 학습 기록입니다.

---

## 📌 학습 목표
- 파이썬 기본 문법 및 자료구조 숙련
- Pythonic한 코드 작성 습관 형성
- 알고리즘 / 코딩 테스트를 위한 기초 체력 확보
- 다른 언어(Java, C#)와의 차이점 이해

---

## 🗂️ 학습 기록

### ✅ Day 01 – Python 기본 자료구조 & 문법 기초
📅 학습일: 2025-12-15  

#### 🔹 학습한 내용
- 변수와 기본 타입
  - `int`, `str`, `bool`
- 리스트(List)
  - 추가: `append`
  - 삭제: `remove`
  - 리스트 컴프리헨션
- 튜플(Tuple)
  - 불변 자료형
  - 구조 분해 할당
- 딕셔너리(Dictionary)
  - Key-Value 구조
  - `items()` 순회
- 집합(Set)
  - 중복 제거
  - `add`
- 조건문
  - `if / elif / else`
- 반복문
  - `for`
- 함수
  - `def`
  - 반환값(`return`)
- 문자열 처리
  - `split`
  - `upper`
  - f-string

---

#### 🔹 예제 코드
```python
numbers = [1, 2, 3]
squares = [n * n for n in numbers]
print(squares)
```
---

### ✅ Day 02 – 리스트 & 문자열 실전 활용
📅 학습일: 2025-12-21  

#### 🔹 학습한 내용
- 리스트(List) 심화
  - 인덱싱 / 슬라이싱
  - `len`, `count`, `sort`, `reverse`
- 문자열(String) 심화
  - 인덱싱 / 슬라이싱
  - `replace`, `strip`
- 리스트 + 문자열 조합 패턴
- 코딩 테스트에서 자주 쓰이는 기본 로직

---

#### 🔹 핵심 문법 정리

##### 📌 리스트 인덱싱 & 슬라이싱
```python
nums = [10, 20, 30, 40, 50]

print(nums[0])      # 10
print(nums[-1])     # 50
print(nums[1:4])    # [20, 30, 40]
```
---

### ✅ Day 03 – 딕셔너리(HashMap) & 빈도수 패턴
📅 학습일: 2025-12-28  

#### 🔹 학습한 내용
- 딕셔너리(Dictionary) 핵심 사용법
  - Key 존재 여부 체크
  - 값 증가 패턴
- 빈도수(Frequency Count) 문제 패턴
- `get()` 메서드 활용
- 문자열 / 리스트 + 딕셔너리 조합
- 코딩 테스트 단골 유형 정리

---

#### 🔹 딕셔너리 기본 패턴

##### 📌 값 증가 기본 패턴 (가장 중요)
```python
counter = {}

items = ["a", "b", "a", "c", "b", "a"]

for item in items:
    if item not in counter:
        counter[item] = 1
    else:
        counter[item] += 1

print(counter)
```
---

### ✅ Day 04 – Stack & Queue (스택 & 큐)
📅 학습일: 2025-12-29

#### 🔹 학습한 내용
- 스택(Stack)과 큐(Queue)의 개념 이해
- LIFO / FIFO 차이 설명 가능
- 파이썬에서 스택과 큐 구현
- 코딩 테스트 단골 문제 대응

### ✅ Day 05 – 문자열(String) & 빈도수(Frequency)
📅 학습일: 2026-01-01

#### 🔹 학습한 내용
- 문자열의 불변성(immutable) 이해
- 문자열 반복 및 슬라이싱 활용
- dict를 활용한 문자/단어 빈도수 계산
- get() 메서드를 이용한 빈도수 처리 패턴 학습
- 가장 많이 등장한 문자 찾기 실습
- 문자열 뒤집기 기본 로직 구현

#### 🔹 핵심 포인트
- 문자열은 수정 불가 → 새 문자열 생성
- 빈도수 문제는 dict 패턴이 정답
- if-else 대신 get() 활용 시 코드 간결
- 문자열 문제는 코딩 테스트에서 매우 높은 출제 빈도
