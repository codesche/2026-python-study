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
