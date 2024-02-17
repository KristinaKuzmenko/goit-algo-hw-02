from collections import deque

s = input("Введіть слово чи рядок ==>  ").lower().replace(" ", "")


def is_palindrom(s):
    s = s.lower().replace(" ", "")
    d = deque(s)

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


if is_palindrom(s):
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")
