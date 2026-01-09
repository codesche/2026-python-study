
# 문자열 뒤집기 - 재귀로 구현
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))