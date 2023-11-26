for i in range(1, 7):
    print('+' * i)
print('---------')


for i in range(6, 0, -1):
    print('+' * i)
print('----------')


b = 6
while b >= 0:
    print('+' * b)
    b -= 1
print('-----------')


a = 0
while a <= 6:
    print('+' * a)
    a += 1
print('---------')


for i in range(1, 7):
    spaces = 6 - i
    print(f"{spaces * ' '}{'+' * i}")
print('----------')


for i in range(7, 0, -1):
    spaces = 7 - i
    print(f"{spaces * ' '}{'+' * i}")
print('-----------')


b = 6
while b > 0:
    spaces = 6 - b
    print(f"{spaces * ' '}{'+' * b}")
    b = b - 1
print('-----------')


b = 0
while b <= 6:
    spaces = 6 - b
    print(f"{spaces * ' '}{'+' * b}")
    b = b + 1