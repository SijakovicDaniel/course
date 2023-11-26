a = 1
while a < 10:
    print('*' * a)
    a = a + 1


print('-------------')


a = 10
while a > 0:
    print('*' * a)
    a = a - 1


print('-------------')


for i in range(1, 10):
    print('*' * i)


print('-------------')


for i in range(10, 0, -1):
    print('*' * i)


print('-------------')


a = 0
while a < 10:
    spaces = 9 - a
    print (f"{spaces * ' '}{'*' * a} ")
    a += 1



print('-------------')

a = 10
while a > 0:
    spaces = 10 - a
    print(f"{spaces * ' '}{'*' * a}")
    a -= 1



