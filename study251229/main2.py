from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

# 앞/뒤 삽입·삭제 모두 O(1)
print(queue.popleft())  # 1
print(queue)            # deque([2, 3])

# 실습 - 최근 값 추적 (Undo 느낌)
history = []

history.append("page1")
history.append("page2")
history.append("page3")

print(history.pop())        # page3
print(history.pop())        # page2