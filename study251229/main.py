
## 스택

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack.pop())
print(stack)

## 괄호 검사 - O(n)
def is_valid_parentheses(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

print(is_valid_parentheses("(())()"))  # True
print(is_valid_parentheses("(()"))     # False
print(is_valid_parentheses("())("))    # False

## Queue (큐) - FIFO
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

# pop(0) → O(n) (앞 요소 제거 시 전부 당겨짐)
print(queue.pop(0))     # 1, 느림