
# Python Basic Warm-up
# 기본 자료구조와 문법을 한 번에 익히기

def main():
    # 1. 변수와 기본 타입
    name = "Python"
    version = 3.12
    is_fun = True

    print(f"{name} {version} is fun? {is_fun}")

    # 2. 리스트 (List)
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    numbers.remove(2)

    print("List:", numbers)

    # 리스트 컴프리핸션
    squares = [n * n for n in numbers]
    print("Squares:", squares)

    # 3. 튜플 (Tuple) - 불변
    point = (10, 20)
    x, y = point
    print("Tuple:", x, y)

    # 4. 딕셔너리 (Dictionary)
    user = {
        "id": 1,
        "name": "Alice",
        "role": "admin"
    }

    # 딕셔너리 순회
    for key, value in user.items():
        print(f"{key} => {value}")

    # 5. 집합 (Set) - 중복 제거
    skills = {"Python", "Java", "Python", "C"}
    skills.add("Go")
    print("Set:", skills)

    # 6. 조건문
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"

    print("Grade:", grade)

    # 7. 반복문
    total = 0
    for n in numbers:
        total += n
    print("Sum:", total)

    # 8. 함수
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Developer"))

    # 9. 문자열 처리
    text = "python is powerful"
    words = text.split()
    upper_words = [w.upper() for w in words]

    print("Words:", words)
    print("Upper:", upper_words)

if __name__ == "__main__":
    main()